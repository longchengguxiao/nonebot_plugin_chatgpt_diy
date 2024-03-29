from setuptools import find_packages, setup
import os
path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(path, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()
    setup(name='nonebot_plugin_chatgpt_diy',  # 包名
          version='0.1.1',  # 版本号
          description='A plugin based on nonebot2, which can chat with users by chatgpt',
          long_description=long_description,
          long_description_content_type="text/markdown",
          author='longchengguxiao',
          author_email='1298919732@qq.com',
          url='http://www.lcgx.space/home',
          include_package_data=True,
          install_requires=[
              "openai>=0.27.2",
              "transformers",
              "nonebot2>=2.0.0a16",
              "nonebot-adapter-onebot>=2.0.0b1",
          ],
          license='AGPL-3.0 License',
          packages=find_packages(),
          platforms=["all"],
          classifiers=['Intended Audience :: Developers',
                       'Operating System :: OS Independent',
                       'Natural Language :: Chinese (Simplified)',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3.8',
                       'Programming Language :: Python :: 3.9',
                       'Topic :: Software Development :: Libraries'
                       ],
          )