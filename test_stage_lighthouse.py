import subprocess
from config import host_stage

path = ["stage.piter-online.net/address",
        "stage.piter-online.net/actions",
        "stage.piter-online.net/orders/tohome",
        "stage.piter-online.net/providers/megafon/rates/domashnij-internet",
        "stage.piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
        "stage.piter-online.net/providers/megafon/rates/internet-i-tv",
        "stage.piter-online.net/providers/megafon/rates/internet-tv-mobile",
        "stage.piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
        "stage.piter-online.net/providers/megafon/rates/online-kinoteatr",
        "stage.piter-online.net/providers/megafon/rates",
        "stage.piter-online.net/providers/megafon",
        "stage.piter-online.net/providers",
        "stage.piter-online.net/rates",
        "stage.piter-online.net/rates/domashnij-internet",
        "stage.piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "stage.piter-online.net/rates/internet-tv-mobile",
        "stage.piter-online.net/rates/domashnij-internet",
        "stage.piter-online.net/rates/internet-i-tv",
        "stage.piter-online.net/rates/nedorogoj-domashnij-internet",
        "stage.piter-online.net/rates/internet-100-mbit",
        "stage.piter-online.net/rates/internet-300-mbit",
        "stage.piter-online.net/rates/internet-500-mbit",
        "stage.piter-online.net/rates/online-kinoteatr",
        "stage.piter-online.net/rates/internet-i-mobilnaya-svyaz",
        "stage.piter-online.net/rates/internet-tv-mobile",
        "stage.piter-online.net/rating",
        "stage.piter-online.net/reviews",
        "stage.piter-online.net/dom/pr-kt-ekaterininskii-d-2-id1016822",
        "stage.piter-online.net/address/красногвардейский-id1199/пр-кт-екатерининский-id290913",
        "stage.piter-online.net/rating/dom-ru",
        "stage.piter-online.net/dom/ul-krilenko-d-45-k3-id159138",
        "stage.piter-online.net/doma-nzl"
        ]
websites_to_check = [
        f"https://{host_stage}@stage.piter-online.net/address",
        f"https://{host_stage}@stage.piter-online.net/actions",
        f"https://{host_stage}@stage.piter-online.net/orders/tohome",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates/domashnij-internet",
        f"https://{host_stage}@stage.piter-online.net/providers/mts/rates/internet-i-mobilnaya-svyaz",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates/internet-i-tv",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates/internet-tv-mobile",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates/nedorogoj-domashnij-internet",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates/online-kinoteatr",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon/rates",
        f"https://{host_stage}@stage.piter-online.net/providers/megafon",
        f"https://{host_stage}@stage.piter-online.net/providers",
        f"https://{host_stage}@stage.piter-online.net/rates",
        f"https://{host_stage}@stage.piter-online.net/rates/domashnij-internet",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-i-mobilnaya-svyaz",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-tv-mobile",
        f"https://{host_stage}@stage.piter-online.net/rates/domashnij-internet",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-i-tv",
        f"https://{host_stage}@stage.piter-online.net/rates/nedorogoj-domashnij-internet",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-100-mbit",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-300-mbit",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-500-mbit",
        f"https://{host_stage}@stage.piter-online.net/rates/online-kinoteatr",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-i-mobilnaya-svyaz",
        f"https://{host_stage}@stage.piter-online.net/rates/internet-tv-mobile",
        f"https://{host_stage}@stage.piter-online.net/rating",
        f"https://{host_stage}@stage.piter-online.net/reviews",
        f"https://{host_stage}@stage.piter-online.net/address/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%B2%D0%B0%D1%80%D0%B4%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1199/%D0%BF%D1%80-%D0%BA%D1%82-%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-id290913/d-2-id1016822",
        f"https://{host_stage}@stage.piter-online.net/address/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D0%B2%D0%B0%D1%80%D0%B4%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-id1199/%D0%BF%D1%80-%D0%BA%D1%82-%D0%B5%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-id290913",
        f"https://{host_stage}@stage.piter-online.net/rating/dom-ru",
        f"https://{host_stage}@stage.piter-online.net/address/%D0%BD%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9-id1204/%D1%83%D0%BB-%D0%BA%D1%80%D1%8B%D0%BB%D0%B5%D0%BD%D0%BA%D0%BE-id268280/d-45-k3-id159138",
        f"https://{host_stage}@stage.piter-online.net/doma-nzl"
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