import glob
import os

assets_path = './assets/images'
posts_path = './_posts'

assets_files = glob.glob(assets_path + '/**/*', recursive=True)
markdown_files = glob.glob(posts_path + '/*')

found_assets = []
for md_path in markdown_files:
    with open(md_path, 'r') as file:
        content = file.read()
        for asset_file in assets_files:
            if asset_file[1:] in content:
                if asset_file not in found_assets:
                    found_assets.append(asset_file)

not_found_assets = set(assets_files) ^ set(found_assets)

for asset in not_found_assets:
    print(asset)

for asset in not_found_assets:
    if os.path.exists(asset) and not os.path.isdir(asset):
        os.remove(asset)