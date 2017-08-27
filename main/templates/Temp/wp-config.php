<?php
/
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'karmi3ph_wp491');

/** MySQL database username */
define('DB_USER', 'karmi3ph_wp491');

/** MySQL database password */
define('DB_PASSWORD', 'Z7738@p]LS');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '73pgnrcwabhnpcfmjgxrw0gjuiwtdfxerhs8bh3nwscojccavdxouzn0g53hahyk');
define('SECURE_AUTH_KEY',  'eipjawfdjzzkwko7fmdmoway59d6qfxg9gnkbxntzina4lslaqitfxsi3ht1ru1q');
define('LOGGED_IN_KEY',    'y2pt72dmqkrxxnpeou45gttiowuzqbw1zo2qcbaioigjc5s4audl6utlabgkj42e');
define('NONCE_KEY',        'm01asxch6eoeqc3pyk8rmiwaixftod54cy5sbkesew7h4nbrkx598qrdacrthuzy');
define('AUTH_SALT',        'rvoqyg5ki6yh2p86b2swhik03g5yy6w3f7bsnarrm0irjggap24qyuqdghkbo5ae');
define('SECURE_AUTH_SALT', 'nbbowiny22d8eevagiaohpfwvpmpnes6iz8awqtqp6wpmyaohnslqesea6mveyrj');
define('LOGGED_IN_SALT',   'i38xh6dggoi7evefolcsphlqwhgstxg2n4tmlfug8hw0ewmh3awyxwuohtcon9q5');
define('NONCE_SALT',       'hm6s7yctqcjsjebb9mydzvsabk5qjr5ckchvghkq8if41jcckxkengpqc9pljynr');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wpsn_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
