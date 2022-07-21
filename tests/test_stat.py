#####################################
# Author: S. A. Owerre
# Date modified: 21/07/2022
# Function: Test for Experimentation
#####################################

import pandas as pd
import pytest
import sys
base_path = ''
sys.path.append(base_path + 'ml-projects/ab-testing/ab-testing/src/')
import statistical_test as expr

@pytest.fixture()
def sample_data_fixture():
    data = pd.DataFrame(
        {'treatment':[1294,1251,1279,1248,
    1274,1240,1264,1232,1263,1220,1254,1218,1251,1210],
    'control':[1284,1274,1272,1264,1256,1256,1254,1250,1242,
    1285,1251,1234, 1290, 1285]
    }
    )
    return data.treatment, data.control

def test_statistical(sample_data_fixture):
    # instantiate the class
    model = expr.StatisticalTest()
    treat_sample, contr_sample = sample_data_fixture

    # test student_ttest method
    t, pval = model.student_ttest(treat_sample, contr_sample)
    assert t != 0
    assert pval < 10

    # test welch_ttest method
    t, pval = model.welch_ttest(treat_sample, contr_sample)
    assert t != 0
    assert pval < 10

    # test mann_whitney_utest method
    u, pval = model.mann_whitney_utest(treat_sample, contr_sample)
    assert u != 0
    assert pval < 10