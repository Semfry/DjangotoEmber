import EmberRouter from '@ember/routing/router';
import config from 'mysiteemberjs/config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function () {
  this.route('favgames')
  this.route('modslists');
  this.route('graphs');
  this.route('modeltimerecordscsvs');
  this.route('modeltotalhours');
});
