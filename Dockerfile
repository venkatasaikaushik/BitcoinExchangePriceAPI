FROM python
copy BitcoinExchangePriceAPI.py /home/
EXPOSE 5000
RUN pip install flask
RUN pip install flask-restful
RUN pip install gevent
RUN pip install requests
CMD python /home/BitcoinExchangePriceAPI.py
