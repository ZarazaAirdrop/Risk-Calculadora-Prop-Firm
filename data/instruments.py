INSTRUMENTS = {
    "EURUSD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/USD", "group": "Forex"},
    "GBPUSD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "GBP/USD", "group": "Forex"},
    "USDJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "USD/JPY", "group": "Forex"},
    "USDCHF": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "USD/CHF", "group": "Forex"},
    "AUDUSD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "AUD/USD", "group": "Forex"},
    "USDCAD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "USD/CAD", "group": "Forex"},
    "NZDUSD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "NZD/USD", "group": "Forex"},
    "EURJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "EUR/JPY", "group": "Forex"},
    "EURGBP": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/GBP", "group": "Forex"},
    "EURCHF": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/CHF", "group": "Forex"},
    "EURAUD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/AUD", "group": "Forex"},
    "EURCAD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/CAD", "group": "Forex"},
    "EURNZD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "EUR/NZD", "group": "Forex"},
    "GBPJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "GBP/JPY", "group": "Forex"},
    "GBPCHF": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "GBP/CHF", "group": "Forex"},
    "GBPAUD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "GBP/AUD", "group": "Forex"},
    "GBPCAD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "GBP/CAD", "group": "Forex"},
    "GBPNZD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "GBP/NZD", "group": "Forex"},
    "AUDJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "AUD/JPY", "group": "Forex"},
    "AUDCAD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "AUD/CAD", "group": "Forex"},
    "AUDCHF": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "AUD/CHF", "group": "Forex"},
    "AUDNZD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "AUD/NZD", "group": "Forex"},
    "NZDJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "NZD/JPY", "group": "Forex"},
    "NZDCAD": {"tipo": "forex", "pip_size": 0.0001, "valor_pip": 10, "label": "NZD/CAD", "group": "Forex"},
    "CADJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "CAD/JPY", "group": "Forex"},
    "CHFJPY": {"tipo": "forex", "pip_size": 0.01, "valor_pip": 10, "label": "CHF/JPY", "group": "Forex"},
    "US30": {"tipo": "index", "pip_size": 1, "valor_pip": 5, "label": "US30 (Dow Jones)", "group": "Indices"},
    "NAS100": {"tipo": "index", "pip_size": 1, "valor_pip": 2, "label": "NAS100 (Nasdaq)", "group": "Indices"},
    "SPX500": {"tipo": "index", "pip_size": 1, "valor_pip": 10, "label": "SPX500 (S&P 500)", "group": "Indices"},
    "DAX40": {"tipo": "index", "pip_size": 1, "valor_pip": 25, "label": "DAX40 (Germany)", "group": "Indices"},
    "FTSE100": {"tipo": "index", "pip_size": 1, "valor_pip": 10, "label": "FTSE100 (UK)", "group": "Indices"},
    "CAC40": {"tipo": "index", "pip_size": 1, "valor_pip": 10, "label": "CAC40 (France)", "group": "Indices"},
    "ASX200": {"tipo": "index", "pip_size": 1, "valor_pip": 25, "label": "ASX200 (Australia)", "group": "Indices"},
    "NIKKEI225": {"tipo": "index", "pip_size": 1, "valor_pip": 10, "label": "NIKKEI225 (Japan)", "group": "Indices"},
    "XAUUSD": {"tipo": "commodity", "pip_size": 0.01, "valor_pip": 1, "label": "XAU/USD (Gold)", "group": "Commodities"},
    "XAGUSD": {"tipo": "commodity", "pip_size": 0.001, "valor_pip": 5, "label": "XAG/USD (Silver)", "group": "Commodities"},
    "XTIUSD": {"tipo": "commodity", "pip_size": 0.01, "valor_pip": 10, "label": "XTI/USD (Crude WTI)", "group": "Commodities"},
    "XBRUSD": {"tipo": "commodity", "pip_size": 0.01, "valor_pip": 10, "label": "XBR/USD (Brent Crude)", "group": "Commodities"},
    "COPPER": {"tipo": "commodity", "pip_size": 0.0001, "valor_pip": 2.5, "label": "Copper", "group": "Commodities"},
    "BTCUSD": {"tipo": "crypto", "pip_size": 1, "valor_pip": 1, "label": "BTC/USD (Bitcoin)", "group": "Crypto"},
    "ETHUSD": {"tipo": "crypto", "pip_size": 0.1, "valor_pip": 1, "label": "ETH/USD (Ethereum)", "group": "Crypto"},
    "LTCUSD": {"tipo": "crypto", "pip_size": 0.01, "valor_pip": 1, "label": "LTC/USD (Litecoin)", "group": "Crypto"},
    "XRPUSD": {"tipo": "crypto", "pip_size": 0.0001, "valor_pip": 1, "label": "XRP/USD (Ripple)", "group": "Crypto"},
    "BCHUSD": {"tipo": "crypto", "pip_size": 0.1, "valor_pip": 1, "label": "BCH/USD (Bitcoin Cash)", "group": "Crypto"},
}


def get_instrument_groups():
    from collections import OrderedDict
    groups = OrderedDict()
    for key, val in INSTRUMENTS.items():
        group = val["group"]
        if group not in groups:
            groups[group] = []
        groups[group].append((key, val["label"]))
    return groups
