# --------
# using scipy, it's kinda big but that should not be a problem
# base-notebook lacks at least numpy, widgets, so...
FROM nbhosting/scipy-notebook

RUN true \
    # latest release of nbautoeval \
 && pip install -U nbautoeval \
    # we use the splitcell extension a lot \
 && jupyter nbextension enable splitcell/splitcell \
    # this one for some exercises \
 && jupyter nbextension enable hide_input/main \
    # w7 comes with quite a few extra deps \
 && pip install plotly chart-studio bokeh \
    # for Taylor \
 && pip install autograd \
    # Fourier \
 && pip install k3d \
    # section on pandas \
 && pip install seaborn \
    # w8 \
 && pip install aiohttp \
   # new library JPL Planetary and Lunar Ephemeris \
 && pip install -U de423 \
   # dependency JPL Planetary and Lunar Ephemeris \
 && pip install -U  jplephem \
 && true