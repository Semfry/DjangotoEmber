import Model, { attr } from '@ember-data/model';

export default class FavgamesModel extends Model {
  @attr url;
  @attr gamename;
  @attr startyear;
}
