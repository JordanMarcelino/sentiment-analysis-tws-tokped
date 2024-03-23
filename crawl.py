import time

import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


def get_data(url) -> list:
    browser_options = ChromeOptions()
    browser_options.headless = True

    driver = Chrome(options=browser_options)
    driver.get(url)

    datas = []

    while True:
        try:
            next = driver.find_elements(
                By.CSS_SELECTOR, ".css-16uzo3v-unf-pagination-item"
            )[1]
            reviews = driver.find_elements(By.CSS_SELECTOR, ".css-1k41fl7")

            for review in reviews:
                try:
                    rating = review.find_element(By.CSS_SELECTOR, ".rating")
                    comment = review.find_element(By.CSS_SELECTOR, ".e1qvo2ff8 > span")

                    datas.append(
                        {
                            "rating": rating.get_attribute("aria-label"),
                            "comment": comment.text,
                        }
                    )
                except Exception:
                    pass

            if next.get_attribute("disable") is not None:
                break

            next.click()
            time.sleep(2)

        except Exception:
            break

    driver.quit()
    return datas


def main():
    data = get_data(
        "https://www.tokopedia.com/pinzyofficial/headset-bluetooth-tws-f9-5-led-smart-display-with-powerbank-f9-5/review"
    )
    df = pd.DataFrame(data)
    print(df.head())

    df.to_csv("tokopedia_tws_f9.csv", index=False)


if __name__ == "__main__":
    main()
