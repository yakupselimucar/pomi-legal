# -*- coding: utf-8 -*-
"""Ana sayfadaki (index.html, pomi(1) fonksiyonu) Pomi karakterinin statik SVG karşılığı.

Blog sayfalarında JavaScript çalıştırmadan aynı logoyu göstermek için üretildi.
index.html'deki pomi() ızgarası değişirse bu dosya yeniden üretilmeli."""

BRAND_BODY = (
  '<rect x="4" y="5" width="8.03" height="1.03" fill="#27223D"/>'
  '<rect x="3" y="6" width="10.03" height="1.03" fill="#27223D"/>'
  '<rect x="2" y="7" width="12.03" height="1.03" fill="#27223D"/>'
  '<rect x="2" y="8" width="12.03" height="1.03" fill="#27223D"/>'
  '<rect x="2" y="9" width="12.03" height="1.03" fill="#27223D"/>'
  '<rect x="2" y="10" width="12.03" height="1.03" fill="#27223D"/>'
  '<rect x="3" y="11" width="10.03" height="1.03" fill="#27223D"/>'
  '<rect x="4" y="12" width="8.03" height="1.03" fill="#27223D"/>'
  '<rect x="4" y="4" width="7.03" height="1.03" fill="#27223D"/>'
  '<rect x="4" y="13" width="7.03" height="1.03" fill="#27223D"/>'
  '<rect x="5" y="5" width="6.03" height="1.03" fill="#E8455B"/>'
  '<rect x="4" y="6" width="8.03" height="1.03" fill="#E8455B"/>'
  '<rect x="3" y="7" width="10.03" height="1.03" fill="#E8455B"/>'
  '<rect x="3" y="8" width="10.03" height="1.03" fill="#E8455B"/>'
  '<rect x="3" y="9" width="10.03" height="1.03" fill="#E8455B"/>'
  '<rect x="3" y="10" width="10.03" height="1.03" fill="#E8455B"/>'
  '<rect x="4" y="11" width="8.03" height="1.03" fill="#E8455B"/>'
  '<rect x="5" y="12" width="6.03" height="1.03" fill="#E8455B"/>'
  '<rect x="9" y="11" width="3.03" height="1.03" fill="#C0344A"/>'
  '<rect x="8" y="12" width="2.03" height="1.03" fill="#C0344A"/>'
  '<rect x="5" y="6" width="2.03" height="1.03" fill="#FF7A8C"/>'
  '<rect x="4" y="7" width="1.03" height="1.03" fill="#FF7A8C"/>'
  '<rect x="7" y="2" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="8" y="2" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="6" y="3" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="7" y="3" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="8" y="3" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="9" y="3" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="7" y="4" width="1.03" height="1.03" fill="#2E9B78"/>'
  '<rect x="8" y="4" width="1.03" height="1.03" fill="#2E9B78"/>'
  '<rect x="5" y="4" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="10" y="4" width="1.03" height="1.03" fill="#46C39A"/>'
  '<rect x="6" y="8" width="1.03" height="1.03" fill="#27223D"/>'
  '<rect x="9" y="8" width="1.03" height="1.03" fill="#27223D"/>'
  '<rect x="6" y="8" width="0.53" height="0.53" fill="#FFFFFF"/>'
  '<rect x="9" y="8" width="0.53" height="0.53" fill="#FFFFFF"/>'
  '<rect x="4" y="9" width="1.03" height="1.03" fill="#FFC2CE"/>'
  '<rect x="11" y="9" width="1.03" height="1.03" fill="#FFC2CE"/>'
  '<rect x="7" y="10" width="1.03" height="1.03" fill="#27223D"/>'
  '<rect x="8" y="10" width="1.03" height="1.03" fill="#27223D"/>'
  '<rect x="6" y="9" width="0.63" height="0.63" fill="#27223D"/>'
  '<rect x="9.4" y="9" width="0.63" height="0.63" fill="#27223D"/>'
)

BRAND_SVG = '<svg viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true">' + BRAND_BODY + "</svg>"
