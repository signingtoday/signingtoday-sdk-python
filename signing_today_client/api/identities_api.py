# coding: utf-8

"""
    Signing Today API

    KlNpZ25pbmcgVG9kYXkqIGVuYWJsZXMgc2VhbWxlc3MgaW50ZWdyYXRpb24gb2YgZGlnaXRhbCBzaWduYXR1cmVzIGludG8gYW55CndlYnNpdGUgYnkgdGhlIHVzZSBvZiBlYXN5IHJlcXVlc3RzIHRvIG91ciBBUEkuIFRoaXMgaXMgdGhlIHNtYXJ0IHdheSBvZgphZGRpbmcgZGlnaXRhbCBzaWduYXR1cmUgc3VwcG9ydCB3aXRoIGEgZ3JlYXQgdXNlciBleHBlcmllbmNlLgoKCipTaWduaW5nIFRvZGF5IEFQSXMqIHVzZSBIVFRQIG1ldGhvZHMgYW5kIGFyZSBSRVNUZnVsIGJhc2VkLCBtb3Jlb3ZlciB0aGV5CmFyZSBwcm90ZWN0ZWQgYnkgYSAqc2VydmVyIHRvIHNlcnZlciBhdXRoZW50aWNhdGlvbiogc3RhbmRhcmQgYnkgdGhlIHVzZSBvZgp0b2tlbnMuCgoKKlNpZ25pbmcgVG9kYXkgQVBJcyogY2FuIGJlIHVzZWQgaW4gdGhlc2UgZW52aXJvbm1lbnRzOgoKCnwgRW52aXJvbm1lbnQgfCBEZXNjcmlwdGlvbiB8IEVuZHBvaW50IHwKfCAtLS0tLS0tLS0tLSB8IC0tLS0tLS0tLS0tIHwgLS0tLS0tLS0gfAp8IFNhbmRib3ggICAgIHwgVGVzdCBlbnZpcm9ubWVudCB8IGBodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbWAgfAp8IExpdmUgICAgICAgIHwgUHJvZHVjdGlvbiBlbnZpcm9ubWVudCB8IGBodHRwczovL2FwaS5zaWduaW5ndG9kYXkuY29tYCB8CgoKRm9yIGV2ZXJ5IHNpbmdsZSByZXF1ZXN0IHRvIFNpZ25pbmcgVG9kYXkgaGFzIHRvIGJlIGRlZmluZWQgdGhlIGZvbGxvd2luZwoqSFRUUCogaGVhZGVyOgotIGBBdXRob3JpemF0aW9uYCwgd2hpY2ggY29udGFpbnMgdGhlIGF1dGhlbnRpY2F0aW9uIHRva2VuLgoKSWYgdGhlIHJlcXVlc3QgaGFzIGEgYm9keSB0aGFuIGFub3RoZXIgKkhUVFAqIGhlYWRlciBpcyByZXF1ZXN0ZWQ6Ci0gYENvbnRlbnQtVHlwZWAsIHdpdGggYGFwcGxpY2F0aW9uL2pzb25gIHZhbHVlLgoKCkZvbGxvd3MgYW4gZXhhbXBsZSBvZiB1c2FnZSB0byBlbnVtZXJhdGUgYWxsIHRoZSB1c2VyIG9mICpteS1vcmcqCm9yZ2FuaXphdGlvbi4KCioqRXhhbXBsZSoqCgpgYGBqc29uCiQgY3VybCBodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbS9hcGkvdjEvbXktb3JnL3VzZXJzIFwKICAgIC1IICdBdXRob3JpemF0aW9uOiBUb2tlbiA8YWNjZXNzLXRva2VuPicKYGBgCgojIyBIVFRQIG1ldGhvZHMgdXNlZAoKQVBJcyB1c2UgdGhlIHJpZ2h0IEhUVFAgdmVyYiBpbiBldmVyeSBzaXR1YXRpb24uCgp8IE1ldGhvZCAgIHwgRGVzY3JpcHRpb24gICAgICAgICAgICAgICAgICAgIHwKfCAtLS0tLS0tLSB8IC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSB8CnwgYEdFVGAgICAgfCBSZXF1ZXN0IGRhdGEgZnJvbSBhIHJlc291cmNlICAgfAp8IGBQT1NUYCAgIHwgU2VuZCBkYXRhIHRvIGNyZWF0ZSBhIHJlc291cmNlIHwKfCBgUFVUYCAgICB8IFVwZGF0ZSBhIHJlc291cmNlICAgICAgICAgICAgICB8CnwgYFBBVENIYCAgfCBQYXJ0aWFsbHkgdXBkYXRlIGEgcmVzb3VyY2UgICAgfAp8IGBERUxFVEVgIHwgRGVsZXRlIGEgcmVzb3Vyc2UgICAgICAgICAgICAgIHwKCgojIyBSZXNwb25zZSBkZWZpbml0aW9uCgpBbGwgdGhlIHJlc3BvbnNlIGFyZSBpbiBKU09OIGZvcm1hdC4KQXMgcmVzcG9uc2UgdG8gYSByZXF1ZXN0IG9mIGFsbCB1c2VycyBvZiBhbiBvcmdhbml6YXRpb24geW91IHdpbGwgaGF2ZSBhCnJlc3VsdCBsaWtlIHRoaXM6CgpgYGBqc29uCnsKICAgICJwYWdpbmF0aW9uIjogewogICAgICAiY291bnQiOiA3NSwKICAgICAgInByZXZpb3VzIjogImh0dHBzOi8vc2FuZGJveC5zaWduaW5ndG9kYXkuY29tL2FwaS92MS9teS1vcmcvdXNlcnM/cGFnZT0xIiwKICAgICAgIm5leHQiOiAiaHR0cHM6Ly9zYW5kYm94LnNpZ25pbmd0b2RheS5jb20vYXBpL3YxL215LW9yZy91c2Vycz9wYWdlPTMiLAogICAgICAicGFnZXMiOiA4LAogICAgICAicGFnZSI6IDIKICAgIH0sCiAgICAibWV0YSI6IHsKICAgICAgImNvZGUiOiAyMDAKICAgIH0sCiAgICAiZGF0YSI6IFsKICAgICAgewogICAgICAgICJpZCI6ICJqZG8iLAogICAgICAgICJzdGF0dXMiOiAiZW5hYmxlZCIsCiAgICAgICAgInR5cGUiOiAiQmFzaWMgdXNlciBhY2NvdW50IiwKICAgICAgICAiZW1haWwiOiBqb2huZG9lQGR1bW15ZW1haWwuY29tLAogICAgICAgICJmaXJzdF9uYW1lIjogIkpvaG4iLAogICAgICAgICJsYXN0X25hbWUiOiAiRG9lIiwKICAgICAgICAid2FsbGV0IjogW10sCiAgICAgICAgImNyZWF0ZWRfYnkiOiAic3lzdGVtIiwKICAgICAgICAib3duZXIiOiBmYWxzZSwKICAgICAgICAiYXV0b21hdGljIjogZmFsc2UsCiAgICAgICAgInJhbyI6IGZhbHNlCiAgICAgIH0sCiAgICAgIC4uLgogICAgXQogIH0KYGBgCgpUaGUgSlNPTiBvZiB0aGUgcmVzcG9uc2UgaXMgbWFkZSBvZiB0aHJlZSBwYXJ0czoKLSBQYWdpbmF0aW9uCi0gTWV0YQotIERhdGEKCiMjIyBQYWdpbmF0aW9uCgoqUGFnaW5hdGlvbiogb2JqZWN0IGFsbG93cyB0byBzcGxpdCB0aGUgcmVzcG9uc2UgaW50byBwYXJ0cyBhbmQgdGhlbiB0bwpyZWJ1aWxkIGl0IHNlcXVlbnRpYWxseSBieSB0aGUgdXNlIG9mIGBuZXh0YCBhbmQgYHByZXZpb3VzYCBwYXJhbWV0ZXJzLCBieQp3aGljaCB5b3UgZ2V0IHByZXZpb3VzIGFuZCBmb2xsb3dpbmcgYmxvY2tzLiBUaGUgKlBhZ2luYXRpb24qIGlzIHByZXNlbnQKb25seSBpZiB0aGUgcmVzcG9uc2UgaXMgYSBsaXN0IG9mIG9iamVjdHMuCgpUaGUgZ2VuZXJhbCBzdHJ1Y3R1cmUgb2YgKlBhZ2luYXRpb24qIG9iamVjdCBpcyB0aGUgZm9sbG93aW5nOgoKYGBganNvbgp7CiAgICAicGFnaW5hdGlvbiI6IHsKICAgICAgImNvdW50IjogNzUsCiAgICAgICJwcmV2aW91cyI6ICJodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbS9hcGkvdjEvbXktb3JnL3VzZXJzP3BhZ2U9MSIsCiAgICAgICJuZXh0IjogImh0dHBzOi8vc2FuZGJveC5zaWduaW5ndG9kYXkuY29tL2FwaS92MS9teS1vcmcvdXNlcnM/cGFnZT0zIiwKICAgICAgInBhZ2VzIjogOCwKICAgICAgInBhZ2UiOiAyCiAgICB9LAogICAgLi4uCiAgfQpgYGAKCiMjIyBNZXRhCgoqTWV0YSogb2JqZWN0IGlzIHVzZWQgdG8gZW5yaWNoIHRoZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgcmVzcG9uc2UuIEluIHRoZQpwcmV2aW91cyBleGFtcGxlLCBhIHN1Y2Nlc3NmdWwgY2FzZSBvZiByZXNwb25zZSwgKk1ldGEqIHdpbGwgaGF2ZSB2YWx1ZQpgc3RhdHVzOiAyWFhgLiBJbiBjYXNlIG9mIHVuc3VjY2Vzc2Z1bCByZXNwb25zZSwgKk1ldGEqIHdpbGwgaGF2ZSBmdXJ0aGVyCmluZm9ybWF0aW9uLCBhcyBmb2xsb3dzOgoKYGBganNvbgp7CiAgICAibWV0YSI6IHsKICAgICAgImNvZGUiOiA8SFRUUCBTVEFUVVMgQ09ERT4sCiAgICAgICJlcnJvcl90eXBlIjogPFNUQVRVUyBDT0RFIERFU0NSSVBUSU9OPiwKICAgICAgImVycm9yX21lc3NhZ2UiOiA8RVJST1IgREVTQ1JJUFRJT04+CiAgICB9CiAgfQpgYGAKCiMjIyBEYXRhCgoqRGF0YSogb2JqZWN0IG91dHB1dHMgYXMgb2JqZWN0IG9yIGxpc3Qgb2YgdGhlbS4gQ29udGFpbnMgdGhlIGV4cGVjdGVkIGRhdGEKYXMgcmVxdWVzdGVkIHRvIHRoZSBBUEkuCgojIyBTZWFyY2ggZmlsdGVycwoKU2VhcmNoIGZpbHRlcnMgb2YgdGhlIEFQSSBoYXZlIHRoZSBmb2xsb3dpbmcgc3RydWN0dXJlOgoKYHdoZXJlX0FUVFJJQlVURU5BTUVgPWBWQUxVRWAKCkluIHRoaXMgd2F5IHlvdSBtYWtlIGEgY2FzZS1zZW5zaXRpdmUgc2VhcmNoIG9mICpWQUxVRSouIFlvdSBjYW4gZXh0ZW5kIGl0CnRocm91Z2ggdGhlIERqYW5nbyBsb29rdXAsIG9idGFpbmluZyBtb3JlIHNwZWNpZmljIGZpbHRlcnMuIEZvciBleGFtcGxlOgoKYHdoZXJlX0FUVFJJQlVURU5BTUVfX0xPT0tVUGA9YFZBTFVFYAoKd2hlcmUgKkxPT0tVUCogY2FuIGJlIHJlcGxhY2VkIHdpdGggYGljb250YWluc2AgdG8gaGF2ZSBhIHBhcnRpYWwgaW5zZW5zaXRpdmUKcmVzZWFyY2gsIHdoZXJlCgpgd2hlcmVfZmlyc3RfbmFtZV9faWNvbnRhaW5zYD1gQ0hhYAoKbWF0Y2hlcyB3aXRoIGV2ZXJ5IHVzZXIgdGhhdCBoYXZlIHRoZSAqY2hhKiBzdHJpbmcgaW4gdGhlaXIgbmFtZSwgd2l0aApubyBkaWZmZXJlbmNlcyBiZXR3ZWVuIGNhcGl0YWwgYW5kIGxvd2VyIGNhc2VzLgoKW0hlcmVdKGh0dHBzOi8vZG9jcy5kamFuZ29wcm9qZWN0LmNvbS9lbi8xLjExL3JlZi9tb2RlbHMvcXVlcnlzZXRzLyNmaWVsZC1sb29rdXBzKQp0aGUgbGlzdCBvZiB0aGUgbG9va3Vwcy4KCiMjIFdlYmhvb2tzCgpTaWduaW5nIFRvZGF5IHN1cHBvcnRzIHdlYmhvb2tzIGZvciB0aGUgdXBkYXRlIG9mIERTVHMgYW5kIGlkZW50aXRpZXMgc3RhdHVzLgpZb3UgY2FuIGNob29zZSBpZiB0byB1c2Ugb3Igbm90IHdlYmhvb2tzIGFuZCBpZiB5b3Ugd2FudCB0byByZWNlaXZlIHVwZGF0ZXMKYWJvdXQgRFNUcyBhbmQvb3IgaWRlbnRpdGllcy4gWW91IGNhbiBjb25maWd1cmF0ZSBpdCBvbiBhcHBsaWNhdGlvbiB0b2tlbgpsZXZlbCwgaW4gdGhlICp3ZWJob29rKiBmaWVsZCwgYXMgZm9sbG93czoKCmBgYGpzb24KIndlYmhvb2tzIjogewogICJkc3QiOiAiVVJMIiwKICAiaWRlbnRpdHkiOiAiVVJMIgogIH0KYGBgCgojIyMgRFNUcyBzdGF0dXMgdXBkYXRlCgpEU1RzIHNlbmQgdGhlIGZvbGxvd2luZyBzdGF0dXMgdXBkYXRlczoKLSAqKkRTVF9TVEFUVVNfQ0hBTkdFRCoqOiB3aGVuZXZlciB0aGUgRFNUIGNoYW5nZXMgaXRzIHN0YXR1cwotICoqU0lHTkFUVVJFX1NUQVRVU19DSEFOR0VEKio6IHdoZW5ldmVyIG9uZSBvZiB0aGUgc2lnbmF0dXJlcyBjaGFuZ2VzIGl0cwpzdGF0dXMKCiMjIyMgRFNUX1NUQVRVU19DSEFOR0VECgpTZW5kcyB0aGUgZm9sbG93aW5nIGluZm9ybWF0aW9uOgoKYGBganNvbgp7CiAgICAibWVzc2FnZSI6ICJEU1RfU1RBVFVTX0NIQU5HRUQiLAogICAgImRhdGEiOiB7CiAgICAgICJzdGF0dXMiOiAiPERTVF9TVEFUVVM+IiwKICAgICAgImRzdCI6ICI8RFNUX0lEPiIsCiAgICAgICJyZWFzb24iOiAiPERTVF9SRUFTT04+IgogICAgfQogIH0KYGBgCgojIyMjIFNJR05BVFVSRV9TVEFUVVNfQ0hBTkdFRAoKU2VuZHMgdGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbjoKCmBgYGpzb24KewogICAgIm1lc3NhZ2UiOiAiU0lHTkFUVVJFX1NUQVRVU19DSEFOR0VEIiwKICAgICJkYXRhIjogewogICAgICAic3RhdHVzIjogIjxTSUdOQVRVUkVfU1RBVFVTPiIsCiAgICAgICJncm91cCI6IDxNRU1CRVJTSElQX0dST1VQX0lOREVYPiwKICAgICAgImRzdCI6IHsKICAgICAgICAiaWQiOiAiPERTVF9JRD4iLAogICAgICAgICJ0aXRsZSI6ICI8RFNUX1RJVExFPiIKICAgICAgfSwKICAgICAgInNpZ25hdHVyZSI6ICI8U0lHTkFUVVJFX0lEPiIsCiAgICAgICJzaWduZXIiOiAiPFNJR05FUl9VU0VSTkFNRT4iLAogICAgICAicG9zaXRpb24iOiAiPFNJR05BVFVSRV9QT1NJVElPTj4iLAogICAgICAiZG9jdW1lbnQiOiB7CiAgICAgICAgImRpc3BsYXlfbmFtZSI6ICI8RE9DVU1FTlRfVElUTEU+IiwKICAgICAgICAiaWQiOiAiPERPQ1VNRU5UX0lEPiIsCiAgICAgICAgIm9yZGVyIjogPERPQ1VNRU5UX0lOREVYPgogICAgICB9LAogICAgICAiYXV0b21hdGljIjogPERFQ0xBUkVTX0lGX1RIRV9TSUdORVJfSVNfQVVUT01BVElDPiwKICAgICAgInBhZ2UiOiAiPFNJR05BVFVSRV9QQUdFPiIKICAgIH0KICB9CmBgYAoKIyMjIElkZW50aXRpZXMgc3RhdHVzIHVwZGF0ZQoKSWRlbnRpdGllcyBzZW5kIHRoZSBmb2xsb3dpbmcgc3RhdHVzIHVwZGF0ZXM6Ci0gKipJREVOVElUWV9SRVFVRVNUX0VOUk9MTEVEKio6IHdoZW5ldmVyIGFuIGlkZW50aXR5IHJlcXVlc3QgaXMgYWN0aXZhdGVkCgojIyMjIElERU5USVRZX1JFUVVFU1RfRU5ST0xMRUQKClNlbmRzIHRoZSBmb2xsb3dpbmcgaW5mb3JtYXRpb246CgpgYGBqc29uCnsKICAgICJtZXNzYWdlIjogIklERU5USVRZX1JFUVVFU1RfRU5ST0xMRUQiLAogICAgImRhdGEiOiB7CiAgICAgICJzdGF0dXMiOiAiPFJFUVVFU1RfU1RBVFVTPiIsCiAgICAgICJyZXF1ZXN0IjogIjxSRVFVRVNUX0lEPiIsCiAgICAgICJ1c2VyIjogIjxBUFBMSUNBTlRfVVNFUk5BTUU+IgogICAgfQogIH0KYGBgCgojIyMgVXJsYmFjawoKU29tZXRpbWVzIG1heSBiZSBuZWNlc3NhcnkgdG8gbWFrZSBhIHJlZGlyZWN0IGFmdGVyIGFuIHVzZXIsIGZyb20gdGhlCnNpZ25hdHVyZSB0cmF5LCBoYXMgY29tcGxldGVkIGhpcyBvcGVyYXRpb25zIG9yIGFjdGl2YXRlZCBhIGNlcnRpZmljYXRlLgoKSWYgc2V0LCByZWRpcmVjdHMgY291bGQgaGFwcGVuIGluIDMgY2FzZXM6Ci0gYWZ0ZXIgYSBzaWduYXR1cmUgb3IgZGVjbGluZQotIGFmdGVyIGEgRFNUIGhhcyBiZWVuIHNpZ25lZCBieSBhbGwgdGhlIHNpZ25lcnMgb3IgY2FuY2VsZWQKLSBhZnRlciB0aGUgYWN0aXZhdGlvbiBvZiBhIGNlcnRpZmljYXRlCgpJbiB0aGUgZmlyc3QgdHdvIGNhc2VzIHRoZSB1cmxiYWNrIHJldHVybnMgdGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbiB0aHJvdWdoCmEgZGF0YSBmb3JtOgotICoqZHN0LWlkKio6IGlkIG9mIHRoZSBEU1QKLSAqKmRzdC11cmwqKjogc2lnbmF0dXJlX3RpY2tldCBvZiB0aGUgc2lnbmF0dXJlCi0gKipkc3Qtc3RhdHVzKio6IGN1cnJlbnQgc3RhdHVzIG9mIHRoZSBEU1QKLSAqKmRzdC1zaWduYXR1cmUtaWQqKjogaWQgb2YgdGhlIHNpZ25hdHVyZQotICoqZHN0LXNpZ25hdHVyZS1zdGF0dXMqKjogY3VycmVudCBzdGF0dXMgb2YgdGhlIHNpZ25hdHVyZQotICoqdXNlcioqOiB1c2VybmFtZSBvZiB0aGUgc2lnbmVyCi0gKipkZWNsaW5lLXJlYXNvbioqOiBpbiBjYXNlIG9mIGEgcmVmdXNlZCBEU1QgY29udGFpbnMgdGhlIHJlYXNvbiBvZiB0aGUKZGVjbGluZQoKSW4gdGhlIGxhc3QgY2FzZSB0aGUgdXJsYmFjayByZXR1cm5zIHRoZSBmb2xsb3dpbmcgaW5mb3JtYXRpb24gdGhyb3VnaCBhCmRhdGEgZm9ybToKLSAqKnVzZXIqKjogdXNlcm5hbWUgb2YgdGhlIHVzZXIgYWN0aXZhdGVkIHRoZSBjZXJ0aWZpY2F0ZQotICoqaWRlbnRpdHktcHJvdmlkZXIqKjogdGhlIHByb3ZpZGVyIGhhcyBiZWVuIHVzZWQgdG8gaXNzdWUgdGhlIGNlcnRpZmljYXRlCi0gKippZGVudGl0eS1yZXF1ZXN0LWlkKio6IGlkIG9mIHRoZSBlbnJvbGxtZW50IHJlcXVlc3QKLSAqKmlkZW50aXR5LWlkKio6IGlkIG9mIHRoZSBuZXcgaWRlbnRpdHkKLSAqKmlkZW50aXR5LWxhYmVsKio6IHRoZSBsYWJlbCBhc3NpZ25lZCB0byB0aGUgaWRlbnRpdHkKLSAqKmlkZW50aXR5LWNlcnRpZmljYXRlKio6IHB1YmxpYyBrZXkgb2YgdGhlIGNlcnRpZmljYXRlCgoK  # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from signing_today_client.api_client import ApiClient
from signing_today_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class IdentitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def associate_appearance(self, organization_id, identity_id, inline_object, **kwargs):  # noqa: E501
        """Associate an appearance to an identity  # noqa: E501

        Associate a signature appearance to an already existing identity through an url to an image. This appearance will be displayed on the document after the signature.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.associate_appearance(organization_id, identity_id, inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param InlineObject inline_object: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.associate_appearance_with_http_info(organization_id, identity_id, inline_object, **kwargs)  # noqa: E501

    def associate_appearance_with_http_info(self, organization_id, identity_id, inline_object, **kwargs):  # noqa: E501
        """Associate an appearance to an identity  # noqa: E501

        Associate a signature appearance to an already existing identity through an url to an image. This appearance will be displayed on the document after the signature.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.associate_appearance_with_http_info(organization_id, identity_id, inline_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param InlineObject inline_object: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'identity_id', 'inline_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method associate_appearance" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `associate_appearance`")  # noqa: E501
        # verify the required parameter 'identity_id' is set
        if ('identity_id' not in local_var_params or
                local_var_params['identity_id'] is None):
            raise ApiValueError("Missing the required parameter `identity_id` when calling `associate_appearance`")  # noqa: E501
        # verify the required parameter 'inline_object' is set
        if ('inline_object' not in local_var_params or
                local_var_params['inline_object'] is None):
            raise ApiValueError("Missing the required parameter `inline_object` when calling `associate_appearance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'identity_id' in local_var_params:
            path_params['identity-id'] = local_var_params['identity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object' in local_var_params:
            body_params = local_var_params['inline_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities/{identity-id}/appearance', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def associate_identity(self, organization_id, user_id, identity_association, **kwargs):  # noqa: E501
        """Associate to an user an already existing identity  # noqa: E501

        Associate to an user of the organization an already existing identity of a provider. The _provider_data_ field is an object and is different for each provider. The minimum set of information to provide as provider_data is the following:   - **aruba**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **aruba-auto**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **infocert**     - _username_ : string     - _password_ : string   - **namirial**     - _id_titolare_ : string     - _id_otp_ : string     - _username_ : string     - _password_ : string   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.associate_identity(organization_id, user_id, identity_association, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param IdentityAssociation identity_association: Provider data to associate (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.associate_identity_with_http_info(organization_id, user_id, identity_association, **kwargs)  # noqa: E501

    def associate_identity_with_http_info(self, organization_id, user_id, identity_association, **kwargs):  # noqa: E501
        """Associate to an user an already existing identity  # noqa: E501

        Associate to an user of the organization an already existing identity of a provider. The _provider_data_ field is an object and is different for each provider. The minimum set of information to provide as provider_data is the following:   - **aruba**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **aruba-auto**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **infocert**     - _username_ : string     - _password_ : string   - **namirial**     - _id_titolare_ : string     - _id_otp_ : string     - _username_ : string     - _password_ : string   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.associate_identity_with_http_info(organization_id, user_id, identity_association, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param IdentityAssociation identity_association: Provider data to associate (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'user_id', 'identity_association']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method associate_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `associate_identity`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ApiValueError("Missing the required parameter `user_id` when calling `associate_identity`")  # noqa: E501
        # verify the required parameter 'identity_association' is set
        if ('identity_association' not in local_var_params or
                local_var_params['identity_association'] is None):
            raise ApiValueError("Missing the required parameter `identity_association` when calling `associate_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['user-id'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'identity_association' in local_var_params:
            body_params = local_var_params['identity_association']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/users/{user-id}/wallet', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_token_from_identity(self, organization_id, create_identityby_token, **kwargs):  # noqa: E501
        """Create an identity from token  # noqa: E501

        This API allows to create an identity from a token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_from_identity(organization_id, create_identityby_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param CreateIdentitybyToken create_identityby_token: Body of the request to create an identity from a token (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_token_from_identity_with_http_info(organization_id, create_identityby_token, **kwargs)  # noqa: E501

    def create_token_from_identity_with_http_info(self, organization_id, create_identityby_token, **kwargs):  # noqa: E501
        """Create an identity from token  # noqa: E501

        This API allows to create an identity from a token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_from_identity_with_http_info(organization_id, create_identityby_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param CreateIdentitybyToken create_identityby_token: Body of the request to create an identity from a token (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2012, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'create_identityby_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_token_from_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `create_token_from_identity`")  # noqa: E501
        # verify the required parameter 'create_identityby_token' is set
        if ('create_identityby_token' not in local_var_params or
                local_var_params['create_identityby_token'] is None):
            raise ApiValueError("Missing the required parameter `create_identityby_token` when calling `create_token_from_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_identityby_token' in local_var_params:
            body_params = local_var_params['create_identityby_token']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities/create/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_appearance(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Delete the appearance of an identity  # noqa: E501

        This API allows to delete the appearance associated to an identity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_appearance(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_appearance_with_http_info(organization_id, identity_id, **kwargs)  # noqa: E501

    def delete_appearance_with_http_info(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Delete the appearance of an identity  # noqa: E501

        This API allows to delete the appearance associated to an identity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_appearance_with_http_info(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2004, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'identity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_appearance" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_appearance`")  # noqa: E501
        # verify the required parameter 'identity_id' is set
        if ('identity_id' not in local_var_params or
                local_var_params['identity_id'] is None):
            raise ApiValueError("Missing the required parameter `identity_id` when calling `delete_appearance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'identity_id' in local_var_params:
            path_params['identity-id'] = local_var_params['identity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities/{identity-id}/appearance', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_enrollment_request(self, organization_id, enrollment_id, **kwargs):  # noqa: E501
        """Delete an enrollment request  # noqa: E501

        This API allows to delete an enrollment request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_enrollment_request(organization_id, enrollment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id enrollment_id: The **enrollment-id** is the uuid code that identifies a specific enrollment request  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_enrollment_request_with_http_info(organization_id, enrollment_id, **kwargs)  # noqa: E501

    def delete_enrollment_request_with_http_info(self, organization_id, enrollment_id, **kwargs):  # noqa: E501
        """Delete an enrollment request  # noqa: E501

        This API allows to delete an enrollment request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_enrollment_request_with_http_info(organization_id, enrollment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id enrollment_id: The **enrollment-id** is the uuid code that identifies a specific enrollment request  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2012, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'enrollment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_enrollment_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_enrollment_request`")  # noqa: E501
        # verify the required parameter 'enrollment_id' is set
        if ('enrollment_id' not in local_var_params or
                local_var_params['enrollment_id'] is None):
            raise ApiValueError("Missing the required parameter `enrollment_id` when calling `delete_enrollment_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'enrollment_id' in local_var_params:
            path_params['enrollment-id'] = local_var_params['enrollment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identity-requests/{enrollment-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_identity(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Delete an identity  # noqa: E501

        This API allows to delete an identity of an user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_identity_with_http_info(organization_id, identity_id, **kwargs)  # noqa: E501

    def delete_identity_with_http_info(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Delete an identity  # noqa: E501

        This API allows to delete an identity of an user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity_with_http_info(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2003, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'identity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_identity`")  # noqa: E501
        # verify the required parameter 'identity_id' is set
        if ('identity_id' not in local_var_params or
                local_var_params['identity_id'] is None):
            raise ApiValueError("Missing the required parameter `identity_id` when calling `delete_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'identity_id' in local_var_params:
            path_params['identity-id'] = local_var_params['identity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities/{identity-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_enrollment_request(self, organization_id, enrollment_id, **kwargs):  # noqa: E501
        """Get information about an enrollment request  # noqa: E501

        This API allows to get information about an enrollment request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_enrollment_request(organization_id, enrollment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id enrollment_id: The **enrollment-id** is the uuid code that identifies a specific enrollment request  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_enrollment_request_with_http_info(organization_id, enrollment_id, **kwargs)  # noqa: E501

    def get_enrollment_request_with_http_info(self, organization_id, enrollment_id, **kwargs):  # noqa: E501
        """Get information about an enrollment request  # noqa: E501

        This API allows to get information about an enrollment request.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_enrollment_request_with_http_info(organization_id, enrollment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id enrollment_id: The **enrollment-id** is the uuid code that identifies a specific enrollment request  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2011, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'enrollment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_enrollment_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `get_enrollment_request`")  # noqa: E501
        # verify the required parameter 'enrollment_id' is set
        if ('enrollment_id' not in local_var_params or
                local_var_params['enrollment_id'] is None):
            raise ApiValueError("Missing the required parameter `enrollment_id` when calling `get_enrollment_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'enrollment_id' in local_var_params:
            path_params['enrollment-id'] = local_var_params['enrollment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identity-requests/{enrollment-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_identity(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Get information about an identity  # noqa: E501

        This API allows to get all the information of an identity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identity(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_identity_with_http_info(organization_id, identity_id, **kwargs)  # noqa: E501

    def get_identity_with_http_info(self, organization_id, identity_id, **kwargs):  # noqa: E501
        """Get information about an identity  # noqa: E501

        This API allows to get all the information of an identity.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identity_with_http_info(organization_id, identity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2002, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'identity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `get_identity`")  # noqa: E501
        # verify the required parameter 'identity_id' is set
        if ('identity_id' not in local_var_params or
                local_var_params['identity_id'] is None):
            raise ApiValueError("Missing the required parameter `identity_id` when calling `get_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'identity_id' in local_var_params:
            path_params['identity-id'] = local_var_params['identity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities/{identity-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_enrollment_requests(self, organization_id, **kwargs):  # noqa: E501
        """Enumerate the enrollment requests of an organization  # noqa: E501

        This API allows to enumerate the enrollment requests of an organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_enrollment_requests(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_provider: Returns the identity requests that have been issued by the specified provider
        :param str where_user: Returns the identity requests of the specified user, searched by its id
        :param str where_first_name: Returns the identity requests of the users that have the specified first name
        :param str where_last_name: Returns the identity requests of the users that have the specified last name
        :param str where_registered_by: Returns the identity requests registered by this user
        :param str where_fiscal_code: Returns the identity requests have the specified fiscal code
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_enrollment_requests_with_http_info(organization_id, **kwargs)  # noqa: E501

    def list_enrollment_requests_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Enumerate the enrollment requests of an organization  # noqa: E501

        This API allows to enumerate the enrollment requests of an organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_enrollment_requests_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_provider: Returns the identity requests that have been issued by the specified provider
        :param str where_user: Returns the identity requests of the specified user, searched by its id
        :param str where_first_name: Returns the identity requests of the users that have the specified first name
        :param str where_last_name: Returns the identity requests of the users that have the specified last name
        :param str where_registered_by: Returns the identity requests registered by this user
        :param str where_fiscal_code: Returns the identity requests have the specified fiscal code
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2005, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'where_provider', 'where_user', 'where_first_name', 'where_last_name', 'where_registered_by', 'where_fiscal_code', 'page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_enrollment_requests" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `list_enrollment_requests`")  # noqa: E501

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_enrollment_requests`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_enrollment_requests`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []
        if 'where_provider' in local_var_params:
            query_params.append(('where_provider', local_var_params['where_provider']))  # noqa: E501
        if 'where_user' in local_var_params:
            query_params.append(('where_user', local_var_params['where_user']))  # noqa: E501
        if 'where_first_name' in local_var_params:
            query_params.append(('where_first_name', local_var_params['where_first_name']))  # noqa: E501
        if 'where_last_name' in local_var_params:
            query_params.append(('where_last_name', local_var_params['where_last_name']))  # noqa: E501
        if 'where_registered_by' in local_var_params:
            query_params.append(('where_registered_by', local_var_params['where_registered_by']))  # noqa: E501
        if 'where_fiscal_code' in local_var_params:
            query_params.append(('where_fiscal_code', local_var_params['where_fiscal_code']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identity-requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_identities(self, organization_id, **kwargs):  # noqa: E501
        """Enumerate the identities of an organization  # noqa: E501

        This API allows to enumerate all the users of an organization. It is possible to filter the data using the supported _django lookups_.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_identities(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_provider: Returns the identities that have been issued by the specified provider
        :param str where_user: Returns the identities of the specified user, searched by its id
        :param str where_first_name: Returns the identities of the users that have the specified first name
        :param str where_last_name: Returns the identities of the users that have the specified last name
        :param str where_registered_by: Returns the identities registered by this user
        :param str where_fiscal_code: Returns the identities that have the specified fiscal code
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_identities_with_http_info(organization_id, **kwargs)  # noqa: E501

    def list_identities_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Enumerate the identities of an organization  # noqa: E501

        This API allows to enumerate all the users of an organization. It is possible to filter the data using the supported _django lookups_.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_identities_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_provider: Returns the identities that have been issued by the specified provider
        :param str where_user: Returns the identities of the specified user, searched by its id
        :param str where_first_name: Returns the identities of the users that have the specified first name
        :param str where_last_name: Returns the identities of the users that have the specified last name
        :param str where_registered_by: Returns the identities registered by this user
        :param str where_fiscal_code: Returns the identities that have the specified fiscal code
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'where_provider', 'where_user', 'where_first_name', 'where_last_name', 'where_registered_by', 'where_fiscal_code', 'page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_identities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `list_identities`")  # noqa: E501

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_identities`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_identities`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []
        if 'where_provider' in local_var_params:
            query_params.append(('where_provider', local_var_params['where_provider']))  # noqa: E501
        if 'where_user' in local_var_params:
            query_params.append(('where_user', local_var_params['where_user']))  # noqa: E501
        if 'where_first_name' in local_var_params:
            query_params.append(('where_first_name', local_var_params['where_first_name']))  # noqa: E501
        if 'where_last_name' in local_var_params:
            query_params.append(('where_last_name', local_var_params['where_last_name']))  # noqa: E501
        if 'where_registered_by' in local_var_params:
            query_params.append(('where_registered_by', local_var_params['where_registered_by']))  # noqa: E501
        if 'where_fiscal_code' in local_var_params:
            query_params.append(('where_fiscal_code', local_var_params['where_fiscal_code']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/identities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_enrollments(self, organization_id, user_id, **kwargs):  # noqa: E501
        """List the enrollments of an user  # noqa: E501

        This API allows to list all the enrollments of an user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_enrollments(organization_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_user_enrollments_with_http_info(organization_id, user_id, **kwargs)  # noqa: E501

    def list_user_enrollments_with_http_info(self, organization_id, user_id, **kwargs):  # noqa: E501
        """List the enrollments of an user  # noqa: E501

        This API allows to list all the enrollments of an user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_enrollments_with_http_info(organization_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2005, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'user_id', 'page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_enrollments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `list_user_enrollments`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ApiValueError("Missing the required parameter `user_id` when calling `list_user_enrollments`")  # noqa: E501

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_user_enrollments`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_user_enrollments`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['user-id'] = local_var_params['user_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/users/{user-id}/identity-requests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_identities(self, organization_id, user_id, **kwargs):  # noqa: E501
        """Enumerate the identities of an user  # noqa: E501

        This API allows to enumerate all the identities of an user, which are located in its wallet.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_identities(organization_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_user_identities_with_http_info(organization_id, user_id, **kwargs)  # noqa: E501

    def list_user_identities_with_http_info(self, organization_id, user_id, **kwargs):  # noqa: E501
        """Enumerate the identities of an user  # noqa: E501

        This API allows to enumerate all the identities of an user, which are located in its wallet.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_identities_with_http_info(organization_id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id user_id: The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  (required)
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'user_id', 'page', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_identities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `list_user_identities`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in local_var_params or
                local_var_params['user_id'] is None):
            raise ApiValueError("Missing the required parameter `user_id` when calling `list_user_identities`")  # noqa: E501

        if 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_user_identities`, must be a value less than or equal to `100`")  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_user_identities`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['user-id'] = local_var_params['user_id']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'count' in local_var_params:
            query_params.append(('count', local_var_params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/users/{user-id}/wallet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_enrollment(self, organization_id, identity_request, **kwargs):  # noqa: E501
        """Submit an enrollment request  # noqa: E501

        This API allows to submit an enrollment request. The user of the request will be created if it does not exists already.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_enrollment(organization_id, identity_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param IdentityRequest identity_request: The enrollment request to submit (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.request_enrollment_with_http_info(organization_id, identity_request, **kwargs)  # noqa: E501

    def request_enrollment_with_http_info(self, organization_id, identity_request, **kwargs):  # noqa: E501
        """Submit an enrollment request  # noqa: E501

        This API allows to submit an enrollment request. The user of the request will be created if it does not exists already.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_enrollment_with_http_info(organization_id, identity_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param IdentityRequest identity_request: The enrollment request to submit (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2011, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'identity_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_enrollment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if ('organization_id' not in local_var_params or
                local_var_params['organization_id'] is None):
            raise ApiValueError("Missing the required parameter `organization_id` when calling `request_enrollment`")  # noqa: E501
        # verify the required parameter 'identity_request' is set
        if ('identity_request' not in local_var_params or
                local_var_params['identity_request'] is None):
            raise ApiValueError("Missing the required parameter `identity_request` when calling `request_enrollment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'identity_request' in local_var_params:
            body_params = local_var_params['identity_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/enroll', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
