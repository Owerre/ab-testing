###############################
# Author: S. A. Owerre
# Date modified: 24/07/2021
# Class: Statistical Tests
###############################

import warnings

warnings.filterwarnings('ignore')
from scipy import stats


class StatisticalTest:
    """Parametric and non-parametric statistical tests."""

    def __init__(self):
        """Define default parameters."""
        pass

    def student_ttest(self, treat_sample, contr_sample):
        """Compute the test statistic and the p-value
        for a two-sample Student's t-test.

        Parameter
        ---------
        treat_sample (Pandas Series): treatment sample
        contr_sample (Pandas Series): control sample

        Return
        ------
        test statistic & p-value
        """
        x = treat_sample.tolist()
        y = contr_sample.tolist()
        t, pval = stats.ttest_ind(
            x, y, equal_var=True, alternative='two-sided'
        )
        return t, pval

    def welch_ttest(self, treat_sample, contr_sample):
        """Compute the test statistic and the p-value
        for a two-sample Welch's t-test.

        Parameter
        ---------
        treat_sample (Pandas Series): treatment sample
        contr_sample (Pandas Series): control sample

        Return
        ------
        test statistic & p-value
        """
        x = treat_sample.tolist()
        y = contr_sample.tolist()
        t, pval = stats.ttest_ind(
            x, y, equal_var=False, alternative='two-sided'
        )
        return t, pval

    def mann_whitney_utest(self, treat_sample, contr_sample):
        """Compute the U statistic and the p-value
        for a two-sample Mann-Whitney U test.

        Parameter
        ---------
        treat_sample (Pandas Series): treatment sample
        contr_sample (Pandas Series): control sample

        Return
        ------
        U statistic & p-value
        """
        x = treat_sample.tolist()
        y = contr_sample.tolist()
        u, pval = stats.mannwhitneyu(
            x, y, use_continuity=True, alternative='two-sided'
        )
        return u, pval
