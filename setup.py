from distutils.core import setup
from os import walk
from 版本 import 版本


def 揣工具包(頭):
    'setup的find_packages無支援windows中文檔案'
    工具包 = []
    for 目錄, _, 檔案 in walk(頭):
        if '__init__.py' in 檔案:
            工具包.append(目錄.replace('/', '.'))
    return 工具包


github網址 = 'https://github.com/i3thuan5/KauTian-IongJi/'


setup(
    name='kau3-tian2_iong7-ji7',
    packages=揣工具包('用字'),
    version=版本,
    description='教典用字',
    long_description='教育部辭典台語用字',
    author='ÌTHUÂN KHOKI',
    author_email='ithuan@ithuan.tw',
    url='https://ithuan.tw',
    download_url=github網址,
    keywords=[
        '語料庫',
        'Taiwan', 'Natural Language', 'Corpus',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django :: 4.2',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    install_requires=[
        'KeSi',
    ],
    package_data={
        '用字': [
            '教典.json',
        ],
    }
)
