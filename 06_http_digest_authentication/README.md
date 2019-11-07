# HTTP Digest Authentication

This is a small demo project in plain html and javascript to illustrate the HTTP digest authentication process.

The goal is to access a private resource located at `https://m183.gibz-informatik.ch/api/httpDigestAuth`. Only these registered users are allowed to access the resource (username : password):
- `britney_s` : `hitMeBaby`
- `bon_jovi` : `badMedicine` 
- `shakira` : `hipsDontLie` 
- `tom_j` : `sexbomb`

The basic authentication process is laied out in the javascript file [scripts/digestAuth.js](scripts/digestAuth.js). It is your task now to complete the implementation.

## Resources
There are many resources you might like to use:
- Script of module 183 (page 36): https://moodle.gibz.ch/moodle/pluginfile.php/15066/mod_resource/content/1/M183%20Skript.pdf
- In-depth Description and security considerations: https://www.securitydrops.com/http-digest/
- Wikipedia article on http digest authentication: https://en.wikipedia.org/wiki/Digest_access_authentication
- RFC 2617 (HTTP Authentication: Basic and Digest Access Authentication): https://tools.ietf.org/html/rfc2617
- Example implementation in PHP: https://gist.github.com/funkatron/949952/11c11ef47f8dab54722ee20dc33372b7417579a6

You are completely free to use any helpful documentation and/or reference implementations. However, you are not allowed to use libraries and/or frameworks of any kind to complete this task!