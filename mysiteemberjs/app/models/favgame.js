import Model, { attr } from '@ember-data/model';

export default class FavgameModel extends Model {
  @attr gamename;
  @attr startyear;
}
