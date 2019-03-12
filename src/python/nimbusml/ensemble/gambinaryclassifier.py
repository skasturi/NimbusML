# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
GamBinaryClassifier
"""

__all__ = ["GamBinaryClassifier"]


from sklearn.base import ClassifierMixin

from ..base_predictor import BasePredictor
from ..internal.core.ensemble.gambinaryclassifier import \
    GamBinaryClassifier as core
from ..internal.utils.utils import trace


class GamBinaryClassifier(core, BasePredictor, ClassifierMixin):
    """

    Generalized Additive Models

    .. remarks::
        `Generalized additive models
        <https://en.wikipedia.org/wiki/Generalized_additive_model>`_
        (referred
        to throughout as GAM) is a class of models expressable as an
        independent
        sum of individual functions. ``nimbusml``'s GAM learner comes in both
        binary
        classification (using logit-boosting) and regression (using least
        squares) flavors.

        In contrast to many formal definitions of GAM, this implementation
        found
        it convenient to represent learning over stepwise functions, which
        betrays the intention that GAM's components be smooth functions. In
        particular: the learner first discretizes features, and the "step"
        functions learned will step between the discretization boundaries.

        This implementation is based on the this `paper
        <https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.352.7619>`_,
        but diverges from it in several important respects: most
        significantly,
        in each round of boosting, rather than do one feature at a time, it
        instead makes a round on all features simultaneously. In each round,
        it
        will choose only one split point of each feature to change.

        In its current form, the GAM learner has the following advantages and
        disadvantages: on the one hand, they offer ready interpretability
        combined with expressive power, but on the other, they are currently
        slow. We would recommend their usage in the case where the key
        criteria
        is interpretability.

        Let's talk a bit more about interpretabilty. The next most
        interpretable
        model, we might say, is a linear model. But really, let's say that
        you
        have a feature with a coefficient of 3.9293, or something. What do
        you
        know? You know that generally, perhaps, larger values for that
        feature
        are "better." Great. But is 4 better than 3? Is 5 better than 4? To
        what
        degree? Are there "shapes" in the distributions hidden because of the
        reduction of a complex quantity to a single values? These are
        questions
        a linear model fundamentally cannot answer, but a GAM model might.


        **Reference**

            `Generalized additive models
            <https://en.wikipedia.org/wiki/Generalized_additive_model>`_,
            `Intelligible Models for Classification and Regression
            <https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.352.7619>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param num_iterations: Total number of iterations over all features.

    :param min_documents: Minimum number of training instances required to form
        a partition.

    :param learning_rate: Determines the size of the step taken in the
        direction of the gradient in each step of the learning process.  This
        determines how fast or slow the learner converges on the optimal
        solution. If the step size is too big, you might overshoot the optimal
        solution.  If the step size is too small, training takes longer to
        converge to the best solution.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param unbalanced_sets: Should we use derivatives optimized for unbalanced
        sets.

    :param entropy_coefficient: The entropy (regularization) coefficient
        between 0 and 1.

    :param gain_conf_level: Tree fitting gain confidence requirement (should be
        in the range [0,1) ).

    :param train_threads: The number of threads to use.

    :param disk_transpose: Whether to utilize the disk or the data's native
        transposition facilities (where applicable) when performing the
        transpose.

    :param num_bins: Maximum number of distinct values (bins) per feature.

    :param max_output: Upper bound on absolute value of single output.

    :param get_derivatives_sample_rate: Sample each query 1 in k times in the
        GetDerivatives function.

    :param random_state: The seed of the random number generator.

    :param feature_flocks: Whether to collectivize features during dataset
        preparation to speed up training.

    :param enable_pruning: Enable post-training pruning to avoid overfitting.
        (a validation set is required).

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`LogisticRegressionMultiClassClassifier
        <nimbusml.linear_model.LogisticRegressionBinaryClassifier>`,
        :py:func:`AveragedPerceptronBinaryClassifier
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`

    .. index:: models, classification, svm

    Example:
       .. literalinclude:: /../nimbusml/examples/GamBinaryClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            num_iterations=9500,
            min_documents=10,
            learning_rate=0.002,
            normalize='Auto',
            caching='Auto',
            unbalanced_sets=False,
            entropy_coefficient=0.0,
            gain_conf_level=0,
            train_threads=None,
            disk_transpose=None,
            num_bins=255,
            max_output=float('inf'),
            get_derivatives_sample_rate=1,
            random_state=123,
            feature_flocks=True,
            enable_pruning=True,
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column' in params:
            raise NameError(
                "'feature_column' must be renamed to 'feature'")
        if feature:
            params['feature_column'] = feature
        if 'label_column' in params:
            raise NameError(
                "'label_column' must be renamed to 'label'")
        if label:
            params['label_column'] = label
        if 'weight_column' in params:
            raise NameError(
                "'weight_column' must be renamed to 'weight'")
        if weight:
            params['weight_column'] = weight
        BasePredictor.__init__(self, type='classifier', **params)
        core.__init__(
            self,
            num_iterations=num_iterations,
            min_documents=min_documents,
            learning_rate=learning_rate,
            normalize=normalize,
            caching=caching,
            unbalanced_sets=unbalanced_sets,
            entropy_coefficient=entropy_coefficient,
            gain_conf_level=gain_conf_level,
            train_threads=train_threads,
            disk_transpose=disk_transpose,
            num_bins=num_bins,
            max_output=max_output,
            get_derivatives_sample_rate=get_derivatives_sample_rate,
            random_state=random_state,
            feature_flocks=feature_flocks,
            enable_pruning=enable_pruning,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    @trace
    def predict_proba(self, X, **params):
        '''
        Returns probabilities
        '''
        return self._predict_proba(X, **params)

    @trace
    def decision_function(self, X, **params):
        '''
        Returns score values
        '''
        return self._decision_function(X, **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
