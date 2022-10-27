import Component from '@glimmer/component';

export default class ModelTotalHoursComponent extends Component {
  chartOptions = {
    chart: {
      type: 'bar'
    },
    title: {
      text: 'Fruit Consumption'
    },
    xAxis: {
      categories: []
    },
    yAxis: {
      title: {
        text: 'Fruit eaten'
      }
    }
  }

  chartData = [{
    name: 'Total Hours',
    data: [1, 2, 5]
  }];
}