import Model, { attr }  from '@ember-data/model';

export default class modeltotalhoursModel extends Model {
  @attr user;
  @attr totalminutes;
  @attr totalhours;
}
