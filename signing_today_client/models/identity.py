# coding: utf-8

"""
    Signing Today API

    KlNpZ25pbmcgVG9kYXkqIGVuYWJsZXMgc2VhbWxlc3MgaW50ZWdyYXRpb24gb2YgZGlnaXRhbCBzaWduYXR1cmVzIGludG8gYW55CndlYnNpdGUgYnkgdGhlIHVzZSBvZiBlYXN5IHJlcXVlc3RzIHRvIG91ciBBUEkuIFRoaXMgaXMgdGhlIHNtYXJ0IHdheSBvZgphZGRpbmcgZGlnaXRhbCBzaWduYXR1cmUgc3VwcG9ydCB3aXRoIGEgZ3JlYXQgdXNlciBleHBlcmllbmNlLgoKCipTaWduaW5nIFRvZGF5IEFQSXMqIHVzZSBIVFRQIG1ldGhvZHMgYW5kIGFyZSBSRVNUZnVsIGJhc2VkLCBtb3Jlb3ZlciB0aGV5CmFyZSBwcm90ZWN0ZWQgYnkgYSAqc2VydmVyIHRvIHNlcnZlciBhdXRoZW50aWNhdGlvbiogc3RhbmRhcmQgYnkgdGhlIHVzZSBvZgp0b2tlbnMuCgoKKlNpZ25pbmcgVG9kYXkgQVBJcyogY2FuIGJlIHVzZWQgaW4gdGhlc2UgZW52aXJvbm1lbnRzOgoKCnwgRW52aXJvbm1lbnQgfCBEZXNjcmlwdGlvbiB8IEVuZHBvaW50IHwKfCAtLS0tLS0tLS0tLSB8IC0tLS0tLS0tLS0tIHwgLS0tLS0tLS0gfAp8IFNhbmRib3ggICAgIHwgVGVzdCBlbnZpcm9ubWVudCB8IGBodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbWAgfAp8IExpdmUgICAgICAgIHwgUHJvZHVjdGlvbiBlbnZpcm9ubWVudCB8IGBodHRwczovL2FwaS5zaWduaW5ndG9kYXkuY29tYCB8CgoKRm9yIGV2ZXJ5IHNpbmdsZSByZXF1ZXN0IHRvIFNpZ25pbmcgVG9kYXkgaGFzIHRvIGJlIGRlZmluZWQgdGhlIGZvbGxvd2luZwoqSFRUUCogaGVhZGVyOgotIGBBdXRob3JpemF0aW9uYCwgd2hpY2ggY29udGFpbnMgdGhlIGF1dGhlbnRpY2F0aW9uIHRva2VuLgoKSWYgdGhlIHJlcXVlc3QgaGFzIGEgYm9keSB0aGFuIGFub3RoZXIgKkhUVFAqIGhlYWRlciBpcyByZXF1ZXN0ZWQ6Ci0gYENvbnRlbnQtVHlwZWAsIHdpdGggYGFwcGxpY2F0aW9uL2pzb25gIHZhbHVlLgoKCkZvbGxvd3MgYW4gZXhhbXBsZSBvZiB1c2FnZSB0byBlbnVtZXJhdGUgYWxsIHRoZSB1c2VyIG9mICpteS1vcmcqCm9yZ2FuaXphdGlvbi4KCioqRXhhbXBsZSoqCgpgYGBqc29uCiQgY3VybCBodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbS9hcGkvdjEvbXktb3JnL3VzZXJzIFwKICAgIC1IICdBdXRob3JpemF0aW9uOiBUb2tlbiA8YWNjZXNzLXRva2VuPicKYGBgCgojIyBIVFRQIG1ldGhvZHMgdXNlZAoKQVBJcyB1c2UgdGhlIHJpZ2h0IEhUVFAgdmVyYiBpbiBldmVyeSBzaXR1YXRpb24uCgp8IE1ldGhvZCAgIHwgRGVzY3JpcHRpb24gICAgICAgICAgICAgICAgICAgIHwKfCAtLS0tLS0tLSB8IC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSB8CnwgYEdFVGAgICAgfCBSZXF1ZXN0IGRhdGEgZnJvbSBhIHJlc291cmNlICAgfAp8IGBQT1NUYCAgIHwgU2VuZCBkYXRhIHRvIGNyZWF0ZSBhIHJlc291cmNlIHwKfCBgUFVUYCAgICB8IFVwZGF0ZSBhIHJlc291cmNlICAgICAgICAgICAgICB8CnwgYFBBVENIYCAgfCBQYXJ0aWFsbHkgdXBkYXRlIGEgcmVzb3VyY2UgICAgfAp8IGBERUxFVEVgIHwgRGVsZXRlIGEgcmVzb3Vyc2UgICAgICAgICAgICAgIHwKCgojIyBSZXNwb25zZSBkZWZpbml0aW9uCgpBbGwgdGhlIHJlc3BvbnNlIGFyZSBpbiBKU09OIGZvcm1hdC4KQXMgcmVzcG9uc2UgdG8gYSByZXF1ZXN0IG9mIGFsbCB1c2VycyBvZiBhbiBvcmdhbml6YXRpb24geW91IHdpbGwgaGF2ZSBhCnJlc3VsdCBsaWtlIHRoaXM6CgpgYGBqc29uCnsKICAgICJwYWdpbmF0aW9uIjogewogICAgICAiY291bnQiOiA3NSwKICAgICAgInByZXZpb3VzIjogImh0dHBzOi8vc2FuZGJveC5zaWduaW5ndG9kYXkuY29tL2FwaS92MS9teS1vcmcvdXNlcnM/cGFnZT0xIiwKICAgICAgIm5leHQiOiAiaHR0cHM6Ly9zYW5kYm94LnNpZ25pbmd0b2RheS5jb20vYXBpL3YxL215LW9yZy91c2Vycz9wYWdlPTMiLAogICAgICAicGFnZXMiOiA4LAogICAgICAicGFnZSI6IDIKICAgIH0sCiAgICAibWV0YSI6IHsKICAgICAgImNvZGUiOiAyMDAKICAgIH0sCiAgICAiZGF0YSI6IFsKICAgICAgewogICAgICAgICJpZCI6ICJqZG8iLAogICAgICAgICJzdGF0dXMiOiAiZW5hYmxlZCIsCiAgICAgICAgInR5cGUiOiAiQmFzaWMgdXNlciBhY2NvdW50IiwKICAgICAgICAiZW1haWwiOiBqb2huZG9lQGR1bW15ZW1haWwuY29tLAogICAgICAgICJmaXJzdF9uYW1lIjogIkpvaG4iLAogICAgICAgICJsYXN0X25hbWUiOiAiRG9lIiwKICAgICAgICAid2FsbGV0IjogW10sCiAgICAgICAgImNyZWF0ZWRfYnkiOiAic3lzdGVtIiwKICAgICAgICAib3duZXIiOiBmYWxzZSwKICAgICAgICAiYXV0b21hdGljIjogZmFsc2UsCiAgICAgICAgInJhbyI6IGZhbHNlCiAgICAgIH0sCiAgICAgIC4uLgogICAgXQogIH0KYGBgCgpUaGUgSlNPTiBvZiB0aGUgcmVzcG9uc2UgaXMgbWFkZSBvZiB0aHJlZSBwYXJ0czoKLSBQYWdpbmF0aW9uCi0gTWV0YQotIERhdGEKCiMjIyBQYWdpbmF0aW9uCgoqUGFnaW5hdGlvbiogb2JqZWN0IGFsbG93cyB0byBzcGxpdCB0aGUgcmVzcG9uc2UgaW50byBwYXJ0cyBhbmQgdGhlbiB0bwpyZWJ1aWxkIGl0IHNlcXVlbnRpYWxseSBieSB0aGUgdXNlIG9mIGBuZXh0YCBhbmQgYHByZXZpb3VzYCBwYXJhbWV0ZXJzLCBieQp3aGljaCB5b3UgZ2V0IHByZXZpb3VzIGFuZCBmb2xsb3dpbmcgYmxvY2tzLiBUaGUgKlBhZ2luYXRpb24qIGlzIHByZXNlbnQKb25seSBpZiB0aGUgcmVzcG9uc2UgaXMgYSBsaXN0IG9mIG9iamVjdHMuCgpUaGUgZ2VuZXJhbCBzdHJ1Y3R1cmUgb2YgKlBhZ2luYXRpb24qIG9iamVjdCBpcyB0aGUgZm9sbG93aW5nOgoKYGBganNvbgp7CiAgICAicGFnaW5hdGlvbiI6IHsKICAgICAgImNvdW50IjogNzUsCiAgICAgICJwcmV2aW91cyI6ICJodHRwczovL3NhbmRib3guc2lnbmluZ3RvZGF5LmNvbS9hcGkvdjEvbXktb3JnL3VzZXJzP3BhZ2U9MSIsCiAgICAgICJuZXh0IjogImh0dHBzOi8vc2FuZGJveC5zaWduaW5ndG9kYXkuY29tL2FwaS92MS9teS1vcmcvdXNlcnM/cGFnZT0zIiwKICAgICAgInBhZ2VzIjogOCwKICAgICAgInBhZ2UiOiAyCiAgICB9LAogICAgLi4uCiAgfQpgYGAKCiMjIyBNZXRhCgoqTWV0YSogb2JqZWN0IGlzIHVzZWQgdG8gZW5yaWNoIHRoZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgcmVzcG9uc2UuIEluIHRoZQpwcmV2aW91cyBleGFtcGxlLCBhIHN1Y2Nlc3NmdWwgY2FzZSBvZiByZXNwb25zZSwgKk1ldGEqIHdpbGwgaGF2ZSB2YWx1ZQpgc3RhdHVzOiAyWFhgLiBJbiBjYXNlIG9mIHVuc3VjY2Vzc2Z1bCByZXNwb25zZSwgKk1ldGEqIHdpbGwgaGF2ZSBmdXJ0aGVyCmluZm9ybWF0aW9uLCBhcyBmb2xsb3dzOgoKYGBganNvbgp7CiAgICAibWV0YSI6IHsKICAgICAgImNvZGUiOiA8SFRUUCBTVEFUVVMgQ09ERT4sCiAgICAgICJlcnJvcl90eXBlIjogPFNUQVRVUyBDT0RFIERFU0NSSVBUSU9OPiwKICAgICAgImVycm9yX21lc3NhZ2UiOiA8RVJST1IgREVTQ1JJUFRJT04+CiAgICB9CiAgfQpgYGAKCiMjIyBEYXRhCgoqRGF0YSogb2JqZWN0IG91dHB1dHMgYXMgb2JqZWN0IG9yIGxpc3Qgb2YgdGhlbS4gQ29udGFpbnMgdGhlIGV4cGVjdGVkIGRhdGEKYXMgcmVxdWVzdGVkIHRvIHRoZSBBUEkuCgojIyBTZWFyY2ggZmlsdGVycwoKU2VhcmNoIGZpbHRlcnMgb2YgdGhlIEFQSSBoYXZlIHRoZSBmb2xsb3dpbmcgc3RydWN0dXJlOgoKYHdoZXJlX0FUVFJJQlVURU5BTUVgPWBWQUxVRWAKCkluIHRoaXMgd2F5IHlvdSBtYWtlIGEgY2FzZS1zZW5zaXRpdmUgc2VhcmNoIG9mICpWQUxVRSouIFlvdSBjYW4gZXh0ZW5kIGl0CnRocm91Z2ggdGhlIERqYW5nbyBsb29rdXAsIG9idGFpbmluZyBtb3JlIHNwZWNpZmljIGZpbHRlcnMuIEZvciBleGFtcGxlOgoKYHdoZXJlX0FUVFJJQlVURU5BTUVfX0xPT0tVUGA9YFZBTFVFYAoKd2hlcmUgKkxPT0tVUCogY2FuIGJlIHJlcGxhY2VkIHdpdGggYGljb250YWluc2AgdG8gaGF2ZSBhIHBhcnRpYWwgaW5zZW5zaXRpdmUKcmVzZWFyY2gsIHdoZXJlCgpgd2hlcmVfZmlyc3RfbmFtZV9faWNvbnRhaW5zYD1gQ0hhYAoKbWF0Y2hlcyB3aXRoIGV2ZXJ5IHVzZXIgdGhhdCBoYXZlIHRoZSAqY2hhKiBzdHJpbmcgaW4gdGhlaXIgbmFtZSwgd2l0aApubyBkaWZmZXJlbmNlcyBiZXR3ZWVuIGNhcGl0YWwgYW5kIGxvd2VyIGNhc2VzLgoKW0hlcmVdKGh0dHBzOi8vZG9jcy5kamFuZ29wcm9qZWN0LmNvbS9lbi8xLjExL3JlZi9tb2RlbHMvcXVlcnlzZXRzLyNmaWVsZC1sb29rdXBzKQp0aGUgbGlzdCBvZiB0aGUgbG9va3Vwcy4KCiMjIFdlYmhvb2tzCgpTaWduaW5nIFRvZGF5IHN1cHBvcnRzIHdlYmhvb2tzIGZvciB0aGUgdXBkYXRlIG9mIERTVHMgYW5kIGlkZW50aXRpZXMgc3RhdHVzLgpZb3UgY2FuIGNob29zZSBpZiB0byB1c2Ugb3Igbm90IHdlYmhvb2tzIGFuZCBpZiB5b3Ugd2FudCB0byByZWNlaXZlIHVwZGF0ZXMKYWJvdXQgRFNUcyBhbmQvb3IgaWRlbnRpdGllcy4gWW91IGNhbiBjb25maWd1cmF0ZSBpdCBvbiBhcHBsaWNhdGlvbiB0b2tlbgpsZXZlbCwgaW4gdGhlICp3ZWJob29rKiBmaWVsZCwgYXMgZm9sbG93czoKCmBgYGpzb24KIndlYmhvb2tzIjogewogICJkc3QiOiAiVVJMIiwKICAiaWRlbnRpdHkiOiAiVVJMIgogIH0KYGBgCgojIyMgRFNUcyBzdGF0dXMgdXBkYXRlCgpEU1RzIHNlbmQgdGhlIGZvbGxvd2luZyBzdGF0dXMgdXBkYXRlczoKLSAqKkRTVF9TVEFUVVNfQ0hBTkdFRCoqOiB3aGVuZXZlciB0aGUgRFNUIGNoYW5nZXMgaXRzIHN0YXR1cwotICoqU0lHTkFUVVJFX1NUQVRVU19DSEFOR0VEKio6IHdoZW5ldmVyIG9uZSBvZiB0aGUgc2lnbmF0dXJlcyBjaGFuZ2VzIGl0cwpzdGF0dXMKCiMjIyMgRFNUX1NUQVRVU19DSEFOR0VECgpTZW5kcyB0aGUgZm9sbG93aW5nIGluZm9ybWF0aW9uOgoKYGBganNvbgp7CiAgICAibWVzc2FnZSI6ICJEU1RfU1RBVFVTX0NIQU5HRUQiLAogICAgImRhdGEiOiB7CiAgICAgICJzdGF0dXMiOiAiPERTVF9TVEFUVVM+IiwKICAgICAgImRzdCI6ICI8RFNUX0lEPiIsCiAgICAgICJyZWFzb24iOiAiPERTVF9SRUFTT04+IgogICAgfQogIH0KYGBgCgojIyMjIFNJR05BVFVSRV9TVEFUVVNfQ0hBTkdFRAoKU2VuZHMgdGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbjoKCmBgYGpzb24KewogICAgIm1lc3NhZ2UiOiAiU0lHTkFUVVJFX1NUQVRVU19DSEFOR0VEIiwKICAgICJkYXRhIjogewogICAgICAic3RhdHVzIjogIjxTSUdOQVRVUkVfU1RBVFVTPiIsCiAgICAgICJncm91cCI6IDxNRU1CRVJTSElQX0dST1VQX0lOREVYPiwKICAgICAgImRzdCI6IHsKICAgICAgICAiaWQiOiAiPERTVF9JRD4iLAogICAgICAgICJ0aXRsZSI6ICI8RFNUX1RJVExFPiIKICAgICAgfSwKICAgICAgInNpZ25hdHVyZSI6ICI8U0lHTkFUVVJFX0lEPiIsCiAgICAgICJzaWduZXIiOiAiPFNJR05FUl9VU0VSTkFNRT4iLAogICAgICAicG9zaXRpb24iOiAiPFNJR05BVFVSRV9QT1NJVElPTj4iLAogICAgICAiZG9jdW1lbnQiOiB7CiAgICAgICAgImRpc3BsYXlfbmFtZSI6ICI8RE9DVU1FTlRfVElUTEU+IiwKICAgICAgICAiaWQiOiAiPERPQ1VNRU5UX0lEPiIsCiAgICAgICAgIm9yZGVyIjogPERPQ1VNRU5UX0lOREVYPgogICAgICB9LAogICAgICAiYXV0b21hdGljIjogPERFQ0xBUkVTX0lGX1RIRV9TSUdORVJfSVNfQVVUT01BVElDPiwKICAgICAgInBhZ2UiOiAiPFNJR05BVFVSRV9QQUdFPiIKICAgIH0KICB9CmBgYAoKIyMjIElkZW50aXRpZXMgc3RhdHVzIHVwZGF0ZQoKSWRlbnRpdGllcyBzZW5kIHRoZSBmb2xsb3dpbmcgc3RhdHVzIHVwZGF0ZXM6Ci0gKipJREVOVElUWV9SRVFVRVNUX0VOUk9MTEVEKio6IHdoZW5ldmVyIGFuIGlkZW50aXR5IHJlcXVlc3QgaXMgYWN0aXZhdGVkCgojIyMjIElERU5USVRZX1JFUVVFU1RfRU5ST0xMRUQKClNlbmRzIHRoZSBmb2xsb3dpbmcgaW5mb3JtYXRpb246CgpgYGBqc29uCnsKICAgICJtZXNzYWdlIjogIklERU5USVRZX1JFUVVFU1RfRU5ST0xMRUQiLAogICAgImRhdGEiOiB7CiAgICAgICJzdGF0dXMiOiAiPFJFUVVFU1RfU1RBVFVTPiIsCiAgICAgICJyZXF1ZXN0IjogIjxSRVFVRVNUX0lEPiIsCiAgICAgICJ1c2VyIjogIjxBUFBMSUNBTlRfVVNFUk5BTUU+IgogICAgfQogIH0KYGBgCgojIyMgVXJsYmFjawoKU29tZXRpbWVzIG1heSBiZSBuZWNlc3NhcnkgdG8gbWFrZSBhIHJlZGlyZWN0IGFmdGVyIGFuIHVzZXIsIGZyb20gdGhlCnNpZ25hdHVyZSB0cmF5LCBoYXMgY29tcGxldGVkIGhpcyBvcGVyYXRpb25zIG9yIGFjdGl2YXRlZCBhIGNlcnRpZmljYXRlLgoKSWYgc2V0LCByZWRpcmVjdHMgY291bGQgaGFwcGVuIGluIDMgY2FzZXM6Ci0gYWZ0ZXIgYSBzaWduYXR1cmUgb3IgZGVjbGluZQotIGFmdGVyIGEgRFNUIGhhcyBiZWVuIHNpZ25lZCBieSBhbGwgdGhlIHNpZ25lcnMgb3IgY2FuY2VsZWQKLSBhZnRlciB0aGUgYWN0aXZhdGlvbiBvZiBhIGNlcnRpZmljYXRlCgpJbiB0aGUgZmlyc3QgdHdvIGNhc2VzIHRoZSB1cmxiYWNrIHJldHVybnMgdGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbiB0aHJvdWdoCmEgZGF0YSBmb3JtOgotICoqZHN0LWlkKio6IGlkIG9mIHRoZSBEU1QKLSAqKmRzdC11cmwqKjogc2lnbmF0dXJlX3RpY2tldCBvZiB0aGUgc2lnbmF0dXJlCi0gKipkc3Qtc3RhdHVzKio6IGN1cnJlbnQgc3RhdHVzIG9mIHRoZSBEU1QKLSAqKmRzdC1zaWduYXR1cmUtaWQqKjogaWQgb2YgdGhlIHNpZ25hdHVyZQotICoqZHN0LXNpZ25hdHVyZS1zdGF0dXMqKjogY3VycmVudCBzdGF0dXMgb2YgdGhlIHNpZ25hdHVyZQotICoqdXNlcioqOiB1c2VybmFtZSBvZiB0aGUgc2lnbmVyCi0gKipkZWNsaW5lLXJlYXNvbioqOiBpbiBjYXNlIG9mIGEgcmVmdXNlZCBEU1QgY29udGFpbnMgdGhlIHJlYXNvbiBvZiB0aGUKZGVjbGluZQoKSW4gdGhlIGxhc3QgY2FzZSB0aGUgdXJsYmFjayByZXR1cm5zIHRoZSBmb2xsb3dpbmcgaW5mb3JtYXRpb24gdGhyb3VnaCBhCmRhdGEgZm9ybToKLSAqKnVzZXIqKjogdXNlcm5hbWUgb2YgdGhlIHVzZXIgYWN0aXZhdGVkIHRoZSBjZXJ0aWZpY2F0ZQotICoqaWRlbnRpdHktcHJvdmlkZXIqKjogdGhlIHByb3ZpZGVyIGhhcyBiZWVuIHVzZWQgdG8gaXNzdWUgdGhlIGNlcnRpZmljYXRlCi0gKippZGVudGl0eS1yZXF1ZXN0LWlkKio6IGlkIG9mIHRoZSBlbnJvbGxtZW50IHJlcXVlc3QKLSAqKmlkZW50aXR5LWlkKio6IGlkIG9mIHRoZSBuZXcgaWRlbnRpdHkKLSAqKmlkZW50aXR5LWxhYmVsKio6IHRoZSBsYWJlbCBhc3NpZ25lZCB0byB0aGUgaWRlbnRpdHkKLSAqKmlkZW50aXR5LWNlcnRpZmljYXRlKio6IHB1YmxpYyBrZXkgb2YgdGhlIGNlcnRpZmljYXRlCgoK  # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Identity(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'actions': 'IdentityActions',
        'certificate': 'str',
        'has_been_imported': 'bool',
        'id': 'str',
        'label': 'str',
        'next': 'str',
        'not_after': 'str',
        'provider': 'str',
        'provider_data': 'object',
        'provider_id': 'str',
        'provider_image': 'str',
        'provider_type': 'str',
        'send_otp_url': 'str',
        'sign_url': 'str',
        'signature_appearance_uri': 'str',
        'status': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'certificate': 'certificate',
        'has_been_imported': 'has_been_imported',
        'id': 'id',
        'label': 'label',
        'next': 'next',
        'not_after': 'not_after',
        'provider': 'provider',
        'provider_data': 'provider_data',
        'provider_id': 'provider_id',
        'provider_image': 'provider_image',
        'provider_type': 'provider_type',
        'send_otp_url': 'send_otp_url',
        'sign_url': 'sign_url',
        'signature_appearance_uri': 'signature_appearance_uri',
        'status': 'status'
    }

    def __init__(self, actions=None, certificate=None, has_been_imported=None, id=None, label=None, next=None, not_after=None, provider=None, provider_data=None, provider_id=None, provider_image=None, provider_type=None, send_otp_url=None, sign_url=None, signature_appearance_uri=None, status=None):  # noqa: E501
        """Identity - a model defined in OpenAPI"""  # noqa: E501

        self._actions = None
        self._certificate = None
        self._has_been_imported = None
        self._id = None
        self._label = None
        self._next = None
        self._not_after = None
        self._provider = None
        self._provider_data = None
        self._provider_id = None
        self._provider_image = None
        self._provider_type = None
        self._send_otp_url = None
        self._sign_url = None
        self._signature_appearance_uri = None
        self._status = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if certificate is not None:
            self.certificate = certificate
        if has_been_imported is not None:
            self.has_been_imported = has_been_imported
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if next is not None:
            self.next = next
        if not_after is not None:
            self.not_after = not_after
        if provider is not None:
            self.provider = provider
        if provider_data is not None:
            self.provider_data = provider_data
        if provider_id is not None:
            self.provider_id = provider_id
        if provider_image is not None:
            self.provider_image = provider_image
        if provider_type is not None:
            self.provider_type = provider_type
        if send_otp_url is not None:
            self.send_otp_url = send_otp_url
        if sign_url is not None:
            self.sign_url = sign_url
        if signature_appearance_uri is not None:
            self.signature_appearance_uri = signature_appearance_uri
        if status is not None:
            self.status = status

    @property
    def actions(self):
        """Gets the actions of this Identity.  # noqa: E501


        :return: The actions of this Identity.  # noqa: E501
        :rtype: IdentityActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Identity.


        :param actions: The actions of this Identity.  # noqa: E501
        :type: IdentityActions
        """

        self._actions = actions

    @property
    def certificate(self):
        """Gets the certificate of this Identity.  # noqa: E501

        The X.509 certificate in PEM format of the Identity  # noqa: E501

        :return: The certificate of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Identity.

        The X.509 certificate in PEM format of the Identity  # noqa: E501

        :param certificate: The certificate of this Identity.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def has_been_imported(self):
        """Gets the has_been_imported of this Identity.  # noqa: E501

        If the Identity has been imported from another pre-existing Identity the has_been_imported field is set to **true**  # noqa: E501

        :return: The has_been_imported of this Identity.  # noqa: E501
        :rtype: bool
        """
        return self._has_been_imported

    @has_been_imported.setter
    def has_been_imported(self, has_been_imported):
        """Sets the has_been_imported of this Identity.

        If the Identity has been imported from another pre-existing Identity the has_been_imported field is set to **true**  # noqa: E501

        :param has_been_imported: The has_been_imported of this Identity.  # noqa: E501
        :type: bool
        """

        self._has_been_imported = has_been_imported

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501

        The uuid code that identifies the Identity  # noqa: E501

        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.

        The uuid code that identifies the Identity  # noqa: E501

        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Identity.  # noqa: E501

        The label is an arbitrary name is possible to associate to an idenity. Doing so allows to distinguish different identities issued from the same provider during the performance of the signature in the signature tray  # noqa: E501

        :return: The label of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Identity.

        The label is an arbitrary name is possible to associate to an idenity. Doing so allows to distinguish different identities issued from the same provider during the performance of the signature in the signature tray  # noqa: E501

        :param label: The label of this Identity.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def next(self):
        """Gets the next of this Identity.  # noqa: E501

        The next step to complete the activation procedure  # noqa: E501

        :return: The next of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Identity.

        The next step to complete the activation procedure  # noqa: E501

        :param next: The next of this Identity.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def not_after(self):
        """Gets the not_after of this Identity.  # noqa: E501

        Deadline of the Identity, expressed in ISO format  # noqa: E501

        :return: The not_after of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this Identity.

        Deadline of the Identity, expressed in ISO format  # noqa: E501

        :param not_after: The not_after of this Identity.  # noqa: E501
        :type: str
        """

        self._not_after = not_after

    @property
    def provider(self):
        """Gets the provider of this Identity.  # noqa: E501

        The name of the provider that issued the certificate for the Identity  # noqa: E501

        :return: The provider of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Identity.

        The name of the provider that issued the certificate for the Identity  # noqa: E501

        :param provider: The provider of this Identity.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def provider_data(self):
        """Gets the provider_data of this Identity.  # noqa: E501

        Data of the provider that issued the certificate, it is variable from provider to provider  # noqa: E501

        :return: The provider_data of this Identity.  # noqa: E501
        :rtype: object
        """
        return self._provider_data

    @provider_data.setter
    def provider_data(self, provider_data):
        """Sets the provider_data of this Identity.

        Data of the provider that issued the certificate, it is variable from provider to provider  # noqa: E501

        :param provider_data: The provider_data of this Identity.  # noqa: E501
        :type: object
        """

        self._provider_data = provider_data

    @property
    def provider_id(self):
        """Gets the provider_id of this Identity.  # noqa: E501

        _provider_id_ is the univocal name of the provider that issued the identity   # noqa: E501

        :return: The provider_id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Identity.

        _provider_id_ is the univocal name of the provider that issued the identity   # noqa: E501

        :param provider_id: The provider_id of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def provider_image(self):
        """Gets the provider_image of this Identity.  # noqa: E501

        This is the logo of the provider that issued the identity  # noqa: E501

        :return: The provider_image of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_image

    @provider_image.setter
    def provider_image(self, provider_image):
        """Sets the provider_image of this Identity.

        This is the logo of the provider that issued the identity  # noqa: E501

        :param provider_image: The provider_image of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_image = provider_image

    @property
    def provider_type(self):
        """Gets the provider_type of this Identity.  # noqa: E501

        Type of the provider. The most usual type is **cloud**   # noqa: E501

        :return: The provider_type of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this Identity.

        Type of the provider. The most usual type is **cloud**   # noqa: E501

        :param provider_type: The provider_type of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def send_otp_url(self):
        """Gets the send_otp_url of this Identity.  # noqa: E501

        The url to send a one time password to the user which the identity is associated  # noqa: E501

        :return: The send_otp_url of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._send_otp_url

    @send_otp_url.setter
    def send_otp_url(self, send_otp_url):
        """Sets the send_otp_url of this Identity.

        The url to send a one time password to the user which the identity is associated  # noqa: E501

        :param send_otp_url: The send_otp_url of this Identity.  # noqa: E501
        :type: str
        """

        self._send_otp_url = send_otp_url

    @property
    def sign_url(self):
        """Gets the sign_url of this Identity.  # noqa: E501

        The url to sign a document of a digital signature transaction  # noqa: E501

        :return: The sign_url of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._sign_url

    @sign_url.setter
    def sign_url(self, sign_url):
        """Sets the sign_url of this Identity.

        The url to sign a document of a digital signature transaction  # noqa: E501

        :param sign_url: The sign_url of this Identity.  # noqa: E501
        :type: str
        """

        self._sign_url = sign_url

    @property
    def signature_appearance_uri(self):
        """Gets the signature_appearance_uri of this Identity.  # noqa: E501

        This is the url to the image that will be impressed on the document after the performance of the signature   # noqa: E501

        :return: The signature_appearance_uri of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._signature_appearance_uri

    @signature_appearance_uri.setter
    def signature_appearance_uri(self, signature_appearance_uri):
        """Sets the signature_appearance_uri of this Identity.

        This is the url to the image that will be impressed on the document after the performance of the signature   # noqa: E501

        :param signature_appearance_uri: The signature_appearance_uri of this Identity.  # noqa: E501
        :type: str
        """

        self._signature_appearance_uri = signature_appearance_uri

    @property
    def status(self):
        """Gets the status of this Identity.  # noqa: E501

        Identity status which can be one of the following. When an identity request is send, the identity is created and the status is **pending** until the provider dont'approve the request. Then status of the identity changes to **active**. If for some reason an error occurs during the process, or after that, the status will be **error**   # noqa: E501

        :return: The status of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Identity.

        Identity status which can be one of the following. When an identity request is send, the identity is created and the status is **pending** until the provider dont'approve the request. Then status of the identity changes to **active**. If for some reason an error occurs during the process, or after that, the status will be **error**   # noqa: E501

        :param status: The status of this Identity.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "active", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
