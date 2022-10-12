import Model, { attr } from '@ember-data/model';

export default class ModlistModel extends Model {
  @attr modname;
  @attr releaseyear;
  @attr game;
  @attr imagelink;
  @attr link;
}
