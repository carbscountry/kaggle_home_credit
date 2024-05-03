from pathlib import Path

from home_credit.utils import ON_KAGGLE

Path('../input/titanic' if ON_KAGGLE else './resources')