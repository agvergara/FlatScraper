from src.selenium_driver import SeleniumScraper


def handler(event=None, context=None):
    driver = SeleniumScraper()

    driver.get("https://www.idealista.com/venta-viviendas/alcorcon/parque-ondarreta-urtinsa/parque-ondarreta-urtinsa/con-precio-hasta_200000,pisos,ultimas-plantas,plantas-intermedias/")
    data = driver.page_source
    driver.close()
    driver.quit()
    response = {
        "statusCode": 200,
        "body": f"{data}",
    }
    print(response)
    return response


if __name__ == "__main__":
    handler()
