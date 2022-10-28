const { Controller } = Ember;

// import Controller from '@ember/controller';

import Ember from 'ember';

import { computed } from '@ember/object';

export default Controller.extend({
    numberData: computed('model', function(){
        return {
            labels: this.get('model').mapBy('user'),
            datasets: [{
                label: 'Total Hours',
                data: this.get('model').mapBy('totalhours')
            }]
        }
    })
})
