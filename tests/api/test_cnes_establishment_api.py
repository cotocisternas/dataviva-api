from test_base import BaseTestCase

class TestCnesEstablishmentApiTests(BaseTestCase):

    def test_should_respond_ok_to_cnes_establishment_path(self):
        response = self.client.get('/cnes_establishment/year/')
        self.assert_200(response)

    def test_should_check_if_all_years_are_loaded(self):
        response = self.client.get('/cnes_establishment/year/?order=year')
        first_year = 2008
        last_year = 2015
        
        data = response.json['data']
        year_index = response.json['headers'].index('year')

        self.assertEqual(data[0][year_index], first_year)
        self.assertEqual(data[-1][year_index], last_year)

        year = first_year
        for item in data:
            self.assertEqual(item[year_index], year)
            year += 1

    def test_should_check_default_headers(self):
        response = self.client.get('/cnes_establishment/year/')
        headers = response.json['headers']
 
        for header in ['year', 'establishments']:
            self.assertIn(header, headers)

    def test_should_check_value_in_2008(self):
        response = self.client.get('/cnes_establishment/year/?year=2008')
        
        data = response.json['data']
        value_index = response.json['headers'].index('establishments')

        self.assertEqual(data[0][value_index], 2157405)
