<?php
define('WP_CACHE', true); // Added by WP Rocket
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
define('DB_NAME', 'karmi3ph_wp24');

/** MySQL database username */
define('DB_USER', 'karmi3ph_wp24');

/** MySQL database password */
define('DB_PASSWORD', 'Wu5!S10cp!');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

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
define('AUTH_KEY',         'vxssg6g06fy7kae0myll3qplmnopfbhcivlilrqozaamakxfcrh1fjlpwlersov2');
define('SECURE_AUTH_KEY',  'h4vz93zdznbfgtemcxodwibri4t7svlhkycstjnn8vpuegeorytvo28bdq9tgr9t');
define('LOGGED_IN_KEY',    '6wzwqjmth1fua8gcacv3hhopvzgocpixvvu30forzw2p1unhshlauwseffunuylz');
define('NONCE_KEY',        'ktmdbehcgcip1nbakqvaobuakkzypyul1ira9fgaljttxxrdknbe2mmcgcmgtmnf');
define('AUTH_SALT',        'vmtwtjwft3etmnzqnr7yfi8b7uatmcj4r7c3rrgeffydairrr1draw7ebzkkdrun');
define('SECURE_AUTH_SALT', 'k9a9dbsurbldt7gv5wgagvzhkeb8cm67z3acuzcamqd9qvwr3tz5chxsjte3ukxx');
define('LOGGED_IN_SALT',   '8vmqym4dluqcdrmq0nvs2c3l7vqc92tb7wfyqljozbo4yvooqx09bmrjzfnogchf');
define('NONCE_SALT',       '6ilwcwf8pccwldgll6vvqw3s2s9qdolw34ezeeuh0zkmkexctkacq2fl8ran20ca');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wpwy_';

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
