# Cover Type
## Predicting forest cover type from cartographic data

The data come from the venerable UCI Machine Learning repository:

https://archive.ics.uci.edu/ml/datasets/covertype

Briefly:

> Predicting forest cover type from cartographic variables only (no remotely
> sensed data). The actual forest cover type for a given observation (30 x 30
> meter cell) was determined from US Forest Service (USFS) Region 2 Resource
> Information System (RIS) data. Independent variables were derived from data
> originally obtained from US Geological Survey (USGS) and USFS data. Data is
> in raw form (not scaled) and contains binary (0 or 1) columns of data for
> qualitative independent variables (wilderness areas and soil types).

The entire process can be run like so: `./run.sh`. Once the refined data are
generated, it is later sufficient just to run `python3 predict.py`. A pickled
model will be saved as `model.pkl` and reused if present in later runs, so it
needs to be removed if any changes are made.

So far I've gotten the best results with one run of `RandomForestClassifier`
with an accuracy of about 90 to 91% but am trying to squeeze a little more
performance out with `GridSearchCV`. More on that later. (**UPDATE**: I
managed about 94%.)
