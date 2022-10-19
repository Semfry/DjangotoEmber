import Model, { attr } from '@ember-data/model';

export default class ModlistModel extends Model {
  @attr url;
  @attr modname;
  @attr releaseyear;
  @attr game;
  @attr image;
  @attr link;
}
