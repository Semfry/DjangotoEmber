import Route from '@ember/routing/route';

import { inject as service } from '@ember/service';

export default Route.extend({
  store: service(),  
  
  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.gamename', '');
    this.controller.set('form.startyear', '');
  },  
  
  actions: {    
    
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');      
      
      const newBook = store.createRecord('favgames', {
        gamename: form.gamename,
        startyear: form.startyear,
      });      
      
      newBook.save()
        .then(() => {
          this.transitionTo('favgames');
        });
    },    
    
    cancel() {
      this.transitionTo('favgames');
    }
  }
});