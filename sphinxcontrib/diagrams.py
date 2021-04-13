# -*- coding: utf-8 -*-
import os
import subprocess

from docutils import nodes
from sphinx.locale import __
from sphinx.transforms.post_transforms.images import ImageConverter, get_filename_for
from sphinx.util import logging
from sphinx.util.osutil import ensuredir

logger = logging.getLogger(__name__)


class DiagramsImageConverter(ImageConverter):
    def convert(self, _from: str, _to: str) -> bool:
        pass

    def is_available(self) -> bool:
        """Confirms the converter is available or not."""
        try:
            args = [self.config.diagrams_exporter_path, '--version']
            logger.debug('Invoking %r ...', args)
            subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except OSError:
            logger.warning(__('convert command %r cannot be run, '
                              'check the diagrams_exporter_path setting'),
                           self.config.diagrams_exporter_path)
            return False
        except subprocess.CalledProcessError as e:
            logger.warning(__('convert exited with error:\n'
                              '[stderr]\n%r\n[stdout]\n%r'),
                           e.stderr, e.stdout)
            return False

    def match(self, node):
        if self.available is None:
            self.available = self.is_available()

        if not self.available:
            return False

        return node.get('uri', '').endswith('.drawio')

    def handle(self, node: nodes.image) -> None:
        # 今は exporter が png/pdf にしか対応していない
        to_mimetype = 'image/png'

        # src
        src_path = node['uri']
        abs_src_path = os.path.join(self.app.srcdir, src_path)

        # dest
        dest_dir = os.path.join(self.imagedir, 'diagrams', os.path.dirname(src_path))
        ensuredir(dest_dir)

        abs_dest_path = os.path.join(dest_dir, get_filename_for(src_path, to_mimetype))
        self.env.original_image_uri[abs_dest_path] = node['uri']

        ret = subprocess.run(
            [
                self.config.diagrams_exporter_path,
                '--format', 'png',
                '-o', abs_dest_path,
                abs_src_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

        if not os.path.isfile(abs_dest_path):
            logger.warning('Fail to convert image: %s (%r %r)', node['uri'], ret.stderr, ret.stdout)

        node['candidates'][to_mimetype] = abs_dest_path
        node['uri'] = abs_dest_path
        self.app.env.images.add_file(self.env.docname, abs_dest_path)


def setup(app):
    app.add_config_value('diagrams_exporter_path', 'drawio', 'html')
    app.add_post_transform(DiagramsImageConverter)
