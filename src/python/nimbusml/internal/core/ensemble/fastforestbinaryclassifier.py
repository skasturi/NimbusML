# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FastForestBinaryClassifier
"""

__all__ = ["FastForestBinaryClassifier"]


from ...entrypoints.trainers_fastforestbinaryclassifier import \
    trainers_fastforestbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class FastForestBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Fast Forest

    .. remarks::
        Decision trees are non-parametric models that perform a sequence of
        simple tests on inputs. This decision procedure maps them to outputs
        found in the training dataset whose inputs were similar to the
        instance
        being processed. A decision is made at each node of the binary tree
        data
        structure based on a measure of similarity that maps each instance
        recursively through the branches of the tree until the appropriate
        leaf
        node is reached and the output decision returned.

        Decision trees have several advantages:

        * They are efficient in both computation and memory usage during
          training and prediction.
        * They can represent non-linear decision boundaries.
        * They perform integrated feature selection and classification.
        * They are resilient in the presence of noisy features.

        Fast forest classifier is a random forest and quantile regression
        forest
        implementation using the tree learner in
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`. The model consists of an
        ensemble of decision trees.


        **Reference**

            `Wikipedia: Random forest
            <https://en.wikipedia.org/wiki/Random_forest>`_

            `Quantile regression forest
            <https://jmlr.org/papers/volume7/meinshausen06a/meinshausen06a.pdf>`_

            `From Stumps to Trees to Forests
            <https://blogs.technet.microsoft.com/machinelearning/2014/09/10/from-
            stumps-to-trees-to-forests/>`_


    :param num_trees: Specifies the total number of decision trees to create in
        the ensemble. By creating more decision trees, you can potentially get
        better coverage, but the training time increases.

    :param num_leaves: The maximum number of leaves (terminal nodes) that can
        be created in any tree. Higher values potentially increase the size of
        the tree and get better precision, but risk overfitting and requiring
        longer training times.

    :param min_split: Minimum number of training instances required to form a
        leaf. That is, the minimal number of documents allowed in a leaf of
        regression tree, out of the sub-sampled data. A 'split' means that
        features in each level of the tree (node) are randomly divided.

    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param max_tree_output: Upper bound on absolute value of single tree
        output.

    :param quantile_sample_count: Number of labels to be sampled from each leaf
        to make the distribtuion.

    :param parallel_trainer: Allows to choose Parallel FastTree Learning
        Algorithm.

    :param train_threads: The number of threads to use.

    :param random_state: The seed of the random number generator.

    :param feature_select_seed: The seed of the active feature selection.

    :param entropy_coefficient: The entropy (regularization) coefficient
        between 0 and 1.

    :param histogram_pool_size: The number of histograms in the pool (between 2
        and numLeaves).

    :param disk_transpose: Whether to utilize the disk or the data's native
        transposition facilities (where applicable) when performing the
        transpose.

    :param feature_flocks: Whether to collectivize features during dataset
        preparation to speed up training.

    :param categorical_split: Whether to do split based on multiple categorical
        feature values.

    :param max_categorical_groups_per_node: Maximum categorical split groups to
        consider when splitting on a categorical feature. Split groups are a
        collection of split points. This is used to reduce overfitting when
        there many categorical features.

    :param max_categorical_split_points: Maximum categorical split points to
        consider when splitting on a categorical feature.

    :param min_docs_percentage_split: Minimum categorical docs percentage in a
        bin to consider for a split.

    :param min_docs_for_categorical_split: Minimum categorical doc count in a
        bin to consider for a split.

    :param bias: Bias for calculating gradient for each feature bin for a
        categorical feature.

    :param bundling: Bundle low population bins. Bundle.None(0): no bundling,
        Bundle.AggregateLowPopulation(1): Bundle low population,
        Bundle.Adjacent(2): Neighbor low population bundle.

    :param num_bins: Maximum number of distinct values (bins) per feature.

    :param sparsify_threshold: Sparsity level needed to use sparse feature
        representation.

    :param first_use_penalty: The feature first use penalty coefficient. This
        is a form of regularization that incurs a penalty for using a new
        feature when creating the tree. Increase this value to create trees
        that don't use many features.

    :param feature_reuse_penalty: The feature re-use penalty (regularization)
        coefficient.

    :param gain_conf_level: Tree fitting gain confidence requirement (should be
        in the range [0,1) ).

    :param softmax_temperature: The temperature of the randomized softmax
        distribution for choosing the feature.

    :param execution_times: Print execution time breakdown to stdout.

    :param feature_fraction: The fraction of features (chosen randomly) to use
        on each iteration.

    :param bagging_size: Number of trees in each bag (0 for disabling bagging).

    :param example_fraction: Percentage of training examples used in each bag.

    :param split_fraction: The fraction of features (chosen randomly) to use on
        each split.

    :param smoothing: Smoothing paramter for tree regularization.

    :param allow_empty_trees: When a root split is impossible, allow training
        to proceed.

    :param feature_compression_level: The level of feature compression to use.

    :param compress_ensemble: Compress the tree Ensemble.

    :param max_trees_after_compression: Maximum Number of trees after
        compression.

    :param test_frequency: Calculate metric values for train/valid/test every k
        rounds.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,
        :py:class:`FastForestRegressor
        <nimbusml.ensemble.FastForestRegressor>`

    .. index:: models, classification, regression

    Example:
       .. literalinclude:: /../nimbusml/examples/FastForestBinaryClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            num_trees=100,
            num_leaves=20,
            min_split=10,
            normalize='Auto',
            caching='Auto',
            max_tree_output=100.0,
            quantile_sample_count=100,
            parallel_trainer=None,
            train_threads=None,
            random_state=123,
            feature_select_seed=123,
            entropy_coefficient=0.0,
            histogram_pool_size=-1,
            disk_transpose=None,
            feature_flocks=True,
            categorical_split=False,
            max_categorical_groups_per_node=64,
            max_categorical_split_points=64,
            min_docs_percentage_split=0.001,
            min_docs_for_categorical_split=100,
            bias=0.0,
            bundling='None',
            num_bins=255,
            sparsify_threshold=0.7,
            first_use_penalty=0.0,
            feature_reuse_penalty=0.0,
            gain_conf_level=0.0,
            softmax_temperature=0.0,
            execution_times=False,
            feature_fraction=0.7,
            bagging_size=1,
            example_fraction=0.7,
            split_fraction=0.7,
            smoothing=0.0,
            allow_empty_trees=True,
            feature_compression_level=1,
            compress_ensemble=False,
            max_trees_after_compression=-1,
            test_frequency=2147483647,
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.num_trees = num_trees
        self.num_leaves = num_leaves
        self.min_split = min_split
        self.normalize = normalize
        self.caching = caching
        self.max_tree_output = max_tree_output
        self.quantile_sample_count = quantile_sample_count
        self.parallel_trainer = parallel_trainer
        self.train_threads = train_threads
        self.random_state = random_state
        self.feature_select_seed = feature_select_seed
        self.entropy_coefficient = entropy_coefficient
        self.histogram_pool_size = histogram_pool_size
        self.disk_transpose = disk_transpose
        self.feature_flocks = feature_flocks
        self.categorical_split = categorical_split
        self.max_categorical_groups_per_node = max_categorical_groups_per_node
        self.max_categorical_split_points = max_categorical_split_points
        self.min_docs_percentage_split = min_docs_percentage_split
        self.min_docs_for_categorical_split = min_docs_for_categorical_split
        self.bias = bias
        self.bundling = bundling
        self.num_bins = num_bins
        self.sparsify_threshold = sparsify_threshold
        self.first_use_penalty = first_use_penalty
        self.feature_reuse_penalty = feature_reuse_penalty
        self.gain_conf_level = gain_conf_level
        self.softmax_temperature = softmax_temperature
        self.execution_times = execution_times
        self.feature_fraction = feature_fraction
        self.bagging_size = bagging_size
        self.example_fraction = example_fraction
        self.split_fraction = split_fraction
        self.smoothing = smoothing
        self.allow_empty_trees = allow_empty_trees
        self.feature_compression_level = feature_compression_level
        self.compress_ensemble = compress_ensemble
        self.max_trees_after_compression = max_trees_after_compression
        self.test_frequency = test_frequency

    @property
    def _entrypoint(self):
        return trainers_fastforestbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role('feature_column', all_args),
            label_column=self._getattr_role('label_column', all_args),
            weight_column=self._getattr_role('weight_column', all_args),
            group_id_column=self._getattr_role('group_id_column', all_args),
            num_trees=self.num_trees,
            num_leaves=self.num_leaves,
            min_documents_in_leafs=self.min_split,
            normalize_features=self.normalize,
            caching=self.caching,
            max_tree_output=self.max_tree_output,
            quantile_sample_count=self.quantile_sample_count,
            parallel_trainer=self.parallel_trainer,
            num_threads=self.train_threads,
            rng_seed=self.random_state,
            feature_select_seed=self.feature_select_seed,
            entropy_coefficient=self.entropy_coefficient,
            histogram_pool_size=self.histogram_pool_size,
            disk_transpose=self.disk_transpose,
            feature_flocks=self.feature_flocks,
            categorical_split=self.categorical_split,
            max_categorical_groups_per_node=self.max_categorical_groups_per_node,
            max_categorical_split_points=self.max_categorical_split_points,
            min_docs_percentage_for_categorical_split=self.min_docs_percentage_split,
            min_docs_for_categorical_split=self.min_docs_for_categorical_split,
            bias=self.bias,
            bundling=self.bundling,
            max_bins=self.num_bins,
            sparsify_threshold=self.sparsify_threshold,
            feature_first_use_penalty=self.first_use_penalty,
            feature_reuse_penalty=self.feature_reuse_penalty,
            gain_confidence_level=self.gain_conf_level,
            softmax_temperature=self.softmax_temperature,
            execution_times=self.execution_times,
            feature_fraction=self.feature_fraction,
            bagging_size=self.bagging_size,
            bagging_train_fraction=self.example_fraction,
            split_fraction=self.split_fraction,
            smoothing=self.smoothing,
            allow_empty_trees=self.allow_empty_trees,
            feature_compression_level=self.feature_compression_level,
            compress_ensemble=self.compress_ensemble,
            max_trees_after_compression=self.max_trees_after_compression,
            test_frequency=self.test_frequency)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
