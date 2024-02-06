# Base stage for installing fonts
FROM pandoc/latex:latest as font_base

WORKDIR /fonts
RUN apk add --no-cache curl unzip && \
    for font in source-sans source-serif source-code-pro; do \
        git_tarball_url="https://www.github.com/adobe-fonts/${font}"$(curl -L "https://github.com/adobe-fonts/${font}/tags" | \
                     grep -o "/archive/refs/tags/.*\.zip" | grep -v 'variable' | sort -r | head -1 | tr -d '\n'); \
        echo "DOWNLOADING FROM: ${git_tarball_url}"; \
        curl -L --retry 5 "${git_tarball_url}" --output "$font.zip"; \
        unzip "${font}.zip"; \
    done && \
    mkdir /adobe-fonts && \
    find /fonts/ -name "*.ttf" -exec install -m644 {} /adobe-fonts/ \; || return 1 && \
    rm -rf /fonts/source*

# Final stage for setting up the environment
FROM pandoc/latex:latest as pandoc_base

# Copy the installed fonts from the font_base stage
COPY --from=font_base /adobe-fonts /usr/share/fonts/adobe-fonts

RUN apk add --no-cache \
    python3 \
    bash \
    py3-pip \
    sed \
    make \
    fontconfig \
    font-noto-cjk \
    freetype \
    && pip3 install --upgrade pip \
    && fc-cache -fv

# Python setup
RUN pip3 install dicttoxml2 setuptools==69.0.3

# Install KOMA-Script and any other necessary LaTeX packages
RUN for i in 1 2 3 4 5; do tlmgr install \
    xecjk \
    ctex \
    fancyhdr \
    hardwrap \
    catchfile \
    ragged2e \
    koma-script \
    setspace \
    colortbl \
    footnotebackref \
    polyglossia \
    pagecolor \
    csquotes \
    caption \
    mdframed \
    needspace \
    titling \
    bookmark \
    newunicodechar \
    adjustbox \
    collectbox \
    listings \
    adjustbox \
    background \
    bidi \
    everypage \
    footmisc \
    fvextra \
    ly1 \
    mweights \
    pagecolor \
    titling \
    ucharcat \
    ulem \
    upquote \
    xurl \
    zref && break || sleep 15; done

# Set the working directory
WORKDIR /data

# Set a neutral default command
ENTRYPOINT [ "make" ]