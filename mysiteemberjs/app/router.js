import EmberRouter from '@ember/routing/router';
import config from 'shaun-site/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function () {
  this.route('favgame');
  this.route('modlist');
});
