import tensorflow as tf

# Basic model parameters.
tf.app.flags.DEFINE_string('game', 'Gridworld-x10-v0',
                           """Bandit experiment type to be run""")
tf.app.flags.DEFINE_string('model_name', "FUN", """Name of the model""")
tf.app.flags.DEFINE_integer('game_size', 10, """Dimension of the gridworld""")
tf.app.flags.DEFINE_integer('game_channels', 3, """Nb of channels for each frame - rgb = 3""")
tf.app.flags.DEFINE_boolean('resume', False,
                            """Resume training from latest checkpoint""")
tf.app.flags.DEFINE_boolean('train', True,
                            """Whether to train or test""")
tf.app.flags.DEFINE_boolean('show_training', False,
                            """Show windows with workers training""")
tf.app.flags.DEFINE_string('checkpoint_dir', './models',
                           """Directory where to save model checkpoints.""")
tf.app.flags.DEFINE_string('summaries_dir', './summaries',
                           """Directory where to write event logs""")
tf.app.flags.DEFINE_string('experiments_dir', './experiments',
                           """Directory where to write event experiments""")
tf.app.flags.DEFINE_string('test_experiments_dir', './test_experiments',
                           """Directory where to write event test experiments""")
tf.app.flags.DEFINE_string('frames_dir', './frames',
                           """Directory where to write event gifs""")
tf.app.flags.DEFINE_boolean('monitor', False,
                            """Monitor test with gym monitor""")
tf.app.flags.DEFINE_integer('summary_interval', 1000, """Number of episodes of interval between summary saves""")
tf.app.flags.DEFINE_integer('checkpoint_interval', 1000, """Number of episodes of interval between checkpoint saves""")
tf.app.flags.DEFINE_integer('nb_actions', 4, """Number of actions to take""")
tf.app.flags.DEFINE_integer('nb_concurrent', 4, """Number of concurrent threads""")
tf.app.flags.DEFINE_integer('explore_steps', 1000000, """explore_steps""")
tf.app.flags.DEFINE_float('initial_random_goal_prob', 0.2, """initial_random_goal_prob""")
tf.app.flags.DEFINE_float('final_random_goal_prob', 0, """final_random_goal_prob""")
tf.app.flags.DEFINE_float('w_gamma', 0.99, """Gamma value""")
tf.app.flags.DEFINE_float('m_gamma', 0.999, """Gamma value""")
tf.app.flags.DEFINE_float('lr', 1e-4, """Learning rate""")
tf.app.flags.DEFINE_float('w_beta_v', 0.5, """Coefficient of value function loss""")
tf.app.flags.DEFINE_float('m_beta_v', 0.5, """Coefficient of value function loss""")
tf.app.flags.DEFINE_float('beta_e', 0.05, """Coefficient of entropy loss""")
tf.app.flags.DEFINE_integer('max_nb_episodes_train', 4000000000, """Max number of episodes of training time""")
tf.app.flags.DEFINE_float('gradient_clip_value', 50.0, """gradient_clip_value""")
tf.app.flags.DEFINE_integer('nb_test_episodes', 150, """Test episodes""")
tf.app.flags.DEFINE_integer('manager_horizon', 8, """manager_horizon = r = c""")
tf.app.flags.DEFINE_integer('K', 400, """manager_horiz = r = c""")
tf.app.flags.DEFINE_integer('goal_embedding_size', 8, """goal_embedding_size""")
tf.app.flags.DEFINE_integer('alpha', 0.5, """manager_horiz = r = c""")