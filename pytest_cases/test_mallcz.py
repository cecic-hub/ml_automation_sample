import pytest
from src.base import commons, base_function as bf


@pytest.mark.usefixtures("setup_web")
class TestMallcz:
    # Assume there are up to 8 carousels on the landing page, each carousel has one test case
    @pytest.mark.parametrize('carousel_number, hooper_number, hp_element_number',
                             [("carousel_one", "hooper_one", "hp_element_one"),
                              ("carousel_two", "hooper_two", "hp_element_two"),
                              ("carousel_three", "hooper_three", "hp_element_three"),
                              ("carousel_four", "hooper_four", "hp_element_four"),
                              ("carousel_five", "hooper_five", "hp_element_five"),
                              ("carousel_six", "hooper_six", "hp_element_six"),
                              ("carousel_seven", "hooper_seven", "hp_element_seven"),
                              ("carousel_eight", "hooper_eight", "hp_element_eight"),
                              ])
    def test_check_carousel(self, extra, carousel_number, hooper_number, hp_element_number):
        print(f"Page title is {self.driver.title}")
        bf.clicks(self.driver, "mcz_landing", "allow_privacy")
        # delete cookies to prevent 403 access denied - cannot load elements issue
        self.driver.delete_all_cookies()
        # scroll down to let the page loaded
        bf.scroll_until_element_exist(self.driver, "mcz_landing", carousel_number, "+ 200")
        # scroll to the carousel
        bf.scroll_at_top(self.driver, "mcz_landing", carousel_number)
        # click all next buttons on the carousel to show all unique elements
        hp_exist = bf.is_element_exist(self.driver, "mcz_landing", hooper_number)
        count = 0
        while hp_exist:
            bf.clicks(self.driver, "mcz_landing", hooper_number)
            count += 1
            print(f"Click hooper times: {count}")
            hp_exist = bf.is_element_exist(self.driver, "mcz_landing", hooper_number)
        print(f"All hoppers are clicked")
        # Check the number of unique elements is 15
        num_unique_ele = len(commons.get_elements(self.driver, "mcz_landing", hp_element_number))
        if num_unique_ele != 15:
            raise Exception(f"Number of unique elements is not 15, actual element is {num_unique_ele}")
        print(f"Number of unique elements is 15")

