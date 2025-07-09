const { add } = require('../src/add');

test('adds numbers', () => {
  expect(add(2, 3)).toBe(5);
});

test('throws on invalid input', () => {
  expect(() => add('a', 1)).toThrow('Invalid input');
});
