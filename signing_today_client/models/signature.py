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


class Signature(object):
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
        'automatic': 'bool',
        'constraints': 'object',
        'declinable': 'bool',
        'decline_url': 'str',
        'description': 'str',
        'description_html': 'str',
        'display_name': 'str',
        'id': 'str',
        'profile': 'str',
        'reason': 'str',
        'signature_ticket': 'str',
        'signer': 'str',
        'signer_group': 'str',
        'status': 'str',
        'urlback': 'str',
        'where': 'SignatureWhere'
    }

    attribute_map = {
        'automatic': 'automatic',
        'constraints': 'constraints',
        'declinable': 'declinable',
        'decline_url': 'decline_url',
        'description': 'description',
        'description_html': 'description_html',
        'display_name': 'display_name',
        'id': 'id',
        'profile': 'profile',
        'reason': 'reason',
        'signature_ticket': 'signature_ticket',
        'signer': 'signer',
        'signer_group': 'signer_group',
        'status': 'status',
        'urlback': 'urlback',
        'where': 'where'
    }

    def __init__(self, automatic=None, constraints=None, declinable=None, decline_url=None, description=None, description_html=None, display_name=None, id=None, profile=None, reason=None, signature_ticket=None, signer=None, signer_group=None, status=None, urlback=None, where=None):  # noqa: E501
        """Signature - a model defined in OpenAPI"""  # noqa: E501

        self._automatic = None
        self._constraints = None
        self._declinable = None
        self._decline_url = None
        self._description = None
        self._description_html = None
        self._display_name = None
        self._id = None
        self._profile = None
        self._reason = None
        self._signature_ticket = None
        self._signer = None
        self._signer_group = None
        self._status = None
        self._urlback = None
        self._where = None
        self.discriminator = None

        if automatic is not None:
            self.automatic = automatic
        if constraints is not None:
            self.constraints = constraints
        if declinable is not None:
            self.declinable = declinable
        if decline_url is not None:
            self.decline_url = decline_url
        if description is not None:
            self.description = description
        if description_html is not None:
            self.description_html = description_html
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if profile is not None:
            self.profile = profile
        if reason is not None:
            self.reason = reason
        if signature_ticket is not None:
            self.signature_ticket = signature_ticket
        if signer is not None:
            self.signer = signer
        if signer_group is not None:
            self.signer_group = signer_group
        if status is not None:
            self.status = status
        if urlback is not None:
            self.urlback = urlback
        if where is not None:
            self.where = where

    @property
    def automatic(self):
        """Gets the automatic of this Signature.  # noqa: E501

        If true indicates that the signer is an _automatic_ one, thus the signature procedure will be different from a regular signer  # noqa: E501

        :return: The automatic of this Signature.  # noqa: E501
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this Signature.

        If true indicates that the signer is an _automatic_ one, thus the signature procedure will be different from a regular signer  # noqa: E501

        :param automatic: The automatic of this Signature.  # noqa: E501
        :type: bool
        """

        self._automatic = automatic

    @property
    def constraints(self):
        """Gets the constraints of this Signature.  # noqa: E501

        Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \"certificate__subject_givenName__iexact=JOHN\"   # noqa: E501

        :return: The constraints of this Signature.  # noqa: E501
        :rtype: object
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this Signature.

        Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \"certificate__subject_givenName__iexact=JOHN\"   # noqa: E501

        :param constraints: The constraints of this Signature.  # noqa: E501
        :type: object
        """

        self._constraints = constraints

    @property
    def declinable(self):
        """Gets the declinable of this Signature.  # noqa: E501

        If true the signer is able to decline the Signature if he wants to  # noqa: E501

        :return: The declinable of this Signature.  # noqa: E501
        :rtype: bool
        """
        return self._declinable

    @declinable.setter
    def declinable(self, declinable):
        """Sets the declinable of this Signature.

        If true the signer is able to decline the Signature if he wants to  # noqa: E501

        :param declinable: The declinable of this Signature.  # noqa: E501
        :type: bool
        """

        self._declinable = declinable

    @property
    def decline_url(self):
        """Gets the decline_url of this Signature.  # noqa: E501

        This is the url to decline a digital signature transaction  # noqa: E501

        :return: The decline_url of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._decline_url

    @decline_url.setter
    def decline_url(self, decline_url):
        """Sets the decline_url of this Signature.

        This is the url to decline a digital signature transaction  # noqa: E501

        :param decline_url: The decline_url of this Signature.  # noqa: E501
        :type: str
        """

        self._decline_url = decline_url

    @property
    def description(self):
        """Gets the description of this Signature.  # noqa: E501

        This is a simple description to attach with the Signature  # noqa: E501

        :return: The description of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Signature.

        This is a simple description to attach with the Signature  # noqa: E501

        :param description: The description of this Signature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_html(self):
        """Gets the description_html of this Signature.  # noqa: E501

        This is a _html_ description to attach with the Signature  # noqa: E501

        :return: The description_html of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._description_html

    @description_html.setter
    def description_html(self, description_html):
        """Sets the description_html of this Signature.

        This is a _html_ description to attach with the Signature  # noqa: E501

        :param description_html: The description_html of this Signature.  # noqa: E501
        :type: str
        """

        self._description_html = description_html

    @property
    def display_name(self):
        """Gets the display_name of this Signature.  # noqa: E501

        This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign  # noqa: E501

        :return: The display_name of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Signature.

        This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign  # noqa: E501

        :param display_name: The display_name of this Signature.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this Signature.  # noqa: E501

        The uuid code that identifies the Signature  # noqa: E501

        :return: The id of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Signature.

        The uuid code that identifies the Signature  # noqa: E501

        :param id: The id of this Signature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def profile(self):
        """Gets the profile of this Signature.  # noqa: E501

        The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ : allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ : allows to sign different types of documents; the signature     is not \"physically\" into the document but the signature and the file     are placed together in an envelope instead, making thus a .p7m extension.   # noqa: E501

        :return: The profile of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Signature.

        The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ : allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ : allows to sign different types of documents; the signature     is not \"physically\" into the document but the signature and the file     are placed together in an envelope instead, making thus a .p7m extension.   # noqa: E501

        :param profile: The profile of this Signature.  # noqa: E501
        :type: str
        """
        allowed_values = ["pades-bes", "pades-t", "cades-bes", "cades-t"]  # noqa: E501
        if profile not in allowed_values:
            raise ValueError(
                "Invalid value for `profile` ({0}), must be one of {1}"  # noqa: E501
                .format(profile, allowed_values)
            )

        self._profile = profile

    @property
    def reason(self):
        """Gets the reason of this Signature.  # noqa: E501

        The reason of the Signature, or rather a motivational description associated to the Signature  # noqa: E501

        :return: The reason of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Signature.

        The reason of the Signature, or rather a motivational description associated to the Signature  # noqa: E501

        :param reason: The reason of this Signature.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def signature_ticket(self):
        """Gets the signature_ticket of this Signature.  # noqa: E501

        This is the url where a signature tray is predisposed for a specific signer that have to sign a specific digital signature transaction  # noqa: E501

        :return: The signature_ticket of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._signature_ticket

    @signature_ticket.setter
    def signature_ticket(self, signature_ticket):
        """Sets the signature_ticket of this Signature.

        This is the url where a signature tray is predisposed for a specific signer that have to sign a specific digital signature transaction  # noqa: E501

        :param signature_ticket: The signature_ticket of this Signature.  # noqa: E501
        :type: str
        """

        self._signature_ticket = signature_ticket

    @property
    def signer(self):
        """Gets the signer of this Signature.  # noqa: E501

        The user that have to sign the digital signature transaction  # noqa: E501

        :return: The signer of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this Signature.

        The user that have to sign the digital signature transaction  # noqa: E501

        :param signer: The signer of this Signature.  # noqa: E501
        :type: str
        """

        self._signer = signer

    @property
    def signer_group(self):
        """Gets the signer_group of this Signature.  # noqa: E501

        The group which the signer belongs. This field is used in the scenario of a digital signature transaction that has multiple signatures to be performed, where the signers belongs to the same group. Let's think to the group _\"teachers\"_ of a school. Thus is possible to add the _signer_group_ _\"teachers\"_ as signers of the digital signature transaction without worrying about who really belong to that group  # noqa: E501

        :return: The signer_group of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._signer_group

    @signer_group.setter
    def signer_group(self, signer_group):
        """Sets the signer_group of this Signature.

        The group which the signer belongs. This field is used in the scenario of a digital signature transaction that has multiple signatures to be performed, where the signers belongs to the same group. Let's think to the group _\"teachers\"_ of a school. Thus is possible to add the _signer_group_ _\"teachers\"_ as signers of the digital signature transaction without worrying about who really belong to that group  # noqa: E501

        :param signer_group: The signer_group of this Signature.  # noqa: E501
        :type: str
        """

        self._signer_group = signer_group

    @property
    def status(self):
        """Gets the status of this Signature.  # noqa: E501

        The status of the Signature. As the digital signature transaction is created the status of the Signature is _waiting_, if everything is legit than the status changes to _pending_, otherwise to _error_. Once the Signature is made the status changes to _performed_. If the DST expires before the Signature is performed then the status changes to _expired_  # noqa: E501

        :return: The status of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Signature.

        The status of the Signature. As the digital signature transaction is created the status of the Signature is _waiting_, if everything is legit than the status changes to _pending_, otherwise to _error_. Once the Signature is made the status changes to _performed_. If the DST expires before the Signature is performed then the status changes to _expired_  # noqa: E501

        :param status: The status of this Signature.  # noqa: E501
        :type: str
        """
        allowed_values = ["waiting", "pending", "performed", "expired", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def urlback(self):
        """Gets the urlback of this Signature.  # noqa: E501

        The url for the redirection from Signature tray when the digital signature transaction is completed or annulled  # noqa: E501

        :return: The urlback of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._urlback

    @urlback.setter
    def urlback(self, urlback):
        """Sets the urlback of this Signature.

        The url for the redirection from Signature tray when the digital signature transaction is completed or annulled  # noqa: E501

        :param urlback: The urlback of this Signature.  # noqa: E501
        :type: str
        """

        self._urlback = urlback

    @property
    def where(self):
        """Gets the where of this Signature.  # noqa: E501


        :return: The where of this Signature.  # noqa: E501
        :rtype: SignatureWhere
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this Signature.


        :param where: The where of this Signature.  # noqa: E501
        :type: SignatureWhere
        """

        self._where = where

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
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
