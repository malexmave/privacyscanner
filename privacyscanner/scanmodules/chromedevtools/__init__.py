from .extractors import FinalUrlExtractor, GoogleAnalyticsExtractor, \
    CookiesExtractor, RequestsExtractor, TLSDetailsExtractor, CertificateExtractor, \
    ThirdPartyExtractor, InsecureContentExtractor, FailedRequestsExtractor, \
    SecurityHeadersExtractor, TrackerDetectExtractor, CookieStatsExtractor, \
    JavaScriptLibsExtractor, ScreenshotExtractor
from .chromescan import ChromeScan

name = 'chromedevtools'
dependencies = []
required_keys = ['site_url']


def scan_site(result, logger, options):
    extractor_classes = [FinalUrlExtractor, GoogleAnalyticsExtractor,
                         CookiesExtractor, RequestsExtractor, TLSDetailsExtractor,
                         CertificateExtractor, ThirdPartyExtractor,
                         InsecureContentExtractor, FailedRequestsExtractor,
                         SecurityHeadersExtractor, TrackerDetectExtractor,
                         CookieStatsExtractor, JavaScriptLibsExtractor,
                         ScreenshotExtractor]
    chrome_scan = ChromeScan(extractor_classes)
    chrome_scan.scan(result, logger, options)
