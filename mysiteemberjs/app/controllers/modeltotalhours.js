const { Controller } = Ember;

import Ember from 'ember';

import { computed } from '@ember/object';

// export default Ember.Controller.extend({
//     numberData: Ember.computed('model', function(){
//         return {
//             labels: this.get('model').mapBy('user'),
//             datasets: [{
//                 label: 'Total Hours',
//                 data: this.get('model').mapBy('totalhours')
//             }]
//         }
//     })
// })

export default Ember.Controller.extend({
    numberData: Ember.computed('model', function() {
        return {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
            }]
        }
    })
})
