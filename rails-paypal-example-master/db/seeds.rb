[
  {
    name: 'Curso Django',
    price: 999
  },
  {
    name: 'Curso Mongodb',
    price: 745
  },
  {
    name: 'Curso Ruby on Rails',
    price: 629
  },
  {
    name: 'Curso Postgres',
    price: 105
  },
  {
    name: 'Curso CSS, SASS y UX',
    price: 588
  },
].each do |product|
  Product.create(product)
end
