import { bubbleChartProcessor, barChartProcessor } from '../processors';


const movement = {
  id: 200,
  date: '2017-06-03',
  amount: '-10',
  amount_current: 'EUR',
  category: 'Category 1',
  sub_category: 'Subcategory 1',
  description: 'This is a movement',
};


it('Verifies Bubble data is processed as expected', () => {
  const processedMovement = bubbleChartProcessor(movement);

  expect(processedMovement.zIndex).toBe('-10');
  expect(processedMovement.data.length).toBe(1);
  expect(processedMovement.data[0].y).toBe(1496448000000);
  expect(processedMovement.data[0].z).toBe(10);
  expect(processedMovement.data[0].name).toBe('Category 1');
  expect(processedMovement.data[0].color).toBe('#FF5722');
  expect(processedMovement.data[0].description).toBe('This is a movement');
});

it('Verifies Bar data is processed as expected', () => {
  const processedMovement = barChartProcessor(movement);

  expect(processedMovement.y).toBe(10);
  expect(processedMovement.x).toBe(1496448000000);
  expect(processedMovement.name).toBe('Category 1');
  expect(processedMovement.color).toBe('#FF5722');
  expect(processedMovement.description).toBe('This is a movement');

});