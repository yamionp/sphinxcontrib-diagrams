FROM sphinxdoc/sphinx
LABEL maintainer="TS&D <yami@crimsondream.jp>"

# Drawio Export
RUN apt-get update \
 && apt-get install -y \
      npm \
      libx11-xcb-dev \
      libxtst6 \
      libasound2 \
      libatk1.0-0 \
      libc6 \
      libcairo2 \
      libcups2 \
      libdbus-1-3 \
      libexpat1 \
      libfontconfig1 \
      libgcc1 \
      libgconf-2-4 \
      libgdk-pixbuf2.0-0 \
      libglib2.0-0 \
      libgtk-3-0 \
      libnspr4 \
      libpango-1.0-0 \
      libpangocairo-1.0-0 \
      libstdc++6 \
      libx11-6 \
      libx11-xcb1 \
      libxcb1 \
      libxcursor1 \
      libxdamage1 \
      libxext6 \
      libxfixes3 \
      libxi6 \
      libxrandr2 \
      libxrender1 \
      libxss1 \
      libxtst6 \
      libnss3 \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN npm -g config set user root
RUN npm install --global draw.io-export
RUN sed s/puppeteer.launch\({/puppeteer.launch\({args:[\'--no-sandbox\',\'--disable-setuid-sandbox\'],/g /usr/local/lib/node_modules/draw.io-export/export.js -i

RUN python3 -m pip install sphinxcontrib-diagrams
