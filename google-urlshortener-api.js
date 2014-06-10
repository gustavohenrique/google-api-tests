var googleapis = require('googleapis'),
    OAuth2 = googleapis.auth.OAuth2;

var CLIENT_ID = 'XXXXXXXXXXX-sstm5956hjjpubosn626fq14r7453nk8.apps.googleusercontent.com',
    CLIENT_SECRET = 'XXXXXXXX_zind4pdol6l',
    REDIRECT_URL = 'http://localhost.localdomain.com:9000';

var oauth2Client = new OAuth2(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL);

var url = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: 'https://www.googleapis.com/auth/plus.me'
});

console.log('Visit the url: ', url);

googleapis
  .discover('urlshortener', 'v1')
  .execute(function(err, client) {
      /*
      client.urlshortener.url.get({ shortUrl: 'http://goo.gl/1ZrQYC' })
        .execute(function(err, result) {
            console.log(result);
        });
      */
      client.urlshortener.url.list().execute(function(err, result) { console.log(err); });
  });
