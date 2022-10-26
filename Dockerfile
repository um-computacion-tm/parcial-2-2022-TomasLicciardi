FROM python
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-TomasLicciardi.git
WORKDIR /parcial-2-2022-TomasLicciardi
COPY . .
CMD ["python", "test.py"]
