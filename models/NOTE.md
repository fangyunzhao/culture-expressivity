Models trained during analysis should live here.

The keras models are stored in `h5` format, which should be stable across package
versions (albeit it is technically deprecated).

All scikit models are pickeled. As pickling is brittle, this requies a specific
version of scikit-learn. Please use `scikit-learn v0.24.1`.
