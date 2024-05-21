import subprocess
path = ["piter-online.net/address",
        "piter-online.net/actions",
        "piter-online.net/orders/tohome",
        "piter-online.net/providers/megafon/rates/domashnij-internet",
        "piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
        "piter-online.net/providers/megafon/rates/internet-i-tv",
        "piter-online.net/providers/megafon/rates/internet-tv-mobile",
        "piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
        "piter-online.net/providers/megafon/rates/online-kinoteatr",
        "piter-online.net/providers/megafon/rates",
        "piter-online.net/providers/megafon",
        "piter-online.net/providers",
        "piter-online.net/rates",
        "piter-online.net/rates/domashnij-internet",
        "piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "piter-online.net/rates/internet-tv-mobile",
        "piter-online.net/rates/domashnij-internet",
        "piter-online.net/rates/internet-i-tv",
        "piter-online.net/rates/nedorogoj-domashnij-internet",
        "piter-online.net/rates/internet-100-mbit",
        "piter-online.net/rates/internet-300-mbit",
        "piter-online.net/rates/internet-500-mbit",
        "piter-online.net/rates/online-kinoteatr",
        "piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "piter-online.net/rates/internet-tv-mobile",
        "piter-online.net/rating",
        "piter-online.net/reviews",
        "piter-online.net/dom/pr-kt-ekaterininskii-d-2-id1016822",
        "piter-online.net/address/красногвардейский-id1199/пр-кт-екатерининский-id290913",
        "piter-online.net/rating/dom-ru",
        "piter-online.net/dom/ul-krilenko-d-45-k3-id159138",
        "piter-online.net/doma-nzl"
        ]

websites_to_check = [
        "https://piter-online.net/address",
        "https://piter-online.net/actions",
        "https://piter-online.net/orders/tohome",
        "https://piter-online.net/providers/megafon/rates/domashnij-internet",
        "https://piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
        "https://piter-online.net/providers/megafon/rates/internet-i-tv",
        "https://piter-online.net/providers/megafon/rates/internet-tv-mobile",
        "https://piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
        "https://piter-online.net/providers/megafon/rates/online-kinoteatr",
        "https://piter-online.net/providers/megafon/rates",
        "https://piter-online.net/providers/megafon",
        "https://piter-online.net/providers",
        "https://piter-online.net/rates",
        "https://piter-online.net/rates/domashnij-internet",
        "https://piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "https://piter-online.net/rates/internet-tv-mobile",
        "https://piter-online.net/rates/domashnij-internet",
        "https://piter-online.net/rates/internet-i-tv",
        "https://piter-online.net/rates/nedorogoj-domashnij-internet",
        "https://piter-online.net/rates/internet-100-mbit",
        "https://piter-online.net/rates/internet-300-mbit",
        "https://piter-online.net/rates/internet-500-mbit",
        "https://piter-online.net/rates/online-kinoteatr",
        "https://piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "https://piter-online.net/rates/internet-tv-mobile",
        "https://piter-online.net/rating",
        "https://piter-online.net/reviews",
        "https://piter-online.net/address/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%B2%D0%B0%D1%80%D0%B4%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1199/%D0%BF%D1%80-%D0%BA%D1%82-%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-id290913/d-2-id1016822",
        "https://piter-online.net/address/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%B2%D0%B0%D1%80%D0%B4%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1199/%D0%BF%D1%80-%D0%BA%D1%82-%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-id290913",
        "https://piter-online.net/rating/dom-ru",
        "https://piter-online.net/address/%D0%BD%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1204/%D1%83%D0%BB-%D0%BA%D1%80%D1%8B%D0%BB%D0%B5%D0%BD%D0%BA%D0%BE-id268280/d-45-k3-id159138",
        "https://piter-online.net/doma-nzl"
    ]


def test_run_lighthouse():
    for i, website_to_check in enumerate(websites_to_check):
        output_path = f"{path[i].replace('/', '_')}.html"  # Using path names for the output
        cmd = f'lighthouse {website_to_check} --output=html --quiet --output-path={output_path}'
        result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            print(f"Lighthouse report for {website_to_check} saved to: {output_path}")
        else:
            print(f"An error occurred while running Lighthouse for {website_to_check}.")