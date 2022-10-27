import Controller from '@ember/controller';

import { computed } from '@ember/object';

// export default Controller.extend({  
    
//     form: computed(function() {
//         return {
//             gamename: '',
//             startyear: '',
//        }
//     })
// });

export default Controller.extend({
    donutData: [
      {
        label: 'Super Cool',
        data: 100
      },
      {
        label: 'Very Cool',
        data: 200
      },
    ],
  });