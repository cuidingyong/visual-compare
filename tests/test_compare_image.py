#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      test_compare_image
   Description:
   Author:          dingyong.cui
   date：           2023/5/6
-------------------------------------------------
   Change Activity:
                    2023/5/6
-------------------------------------------------
"""


class TestCompareImage:

    def setup(self):
        from doc.visual_test import VisualTest
        self.cls = VisualTest

    def test_compare_images(self):
        from doc.image.image import MatchImg
        img1 = '../files/images/123.png'
        img11 = '../files/images/000.png'
        img2 = '../files/images/124.png'
        mi = MatchImg(img1, img11)
        mask = mi.mask
        self.cls().compare_images(img1, img2, mask=mask)

    def test_compare_pdf(self):
        from doc.image.image import MatchImg
        img1 = '../files/images/sample_1_page.pdf'
        # img11 = '../files/images/000.png'
        img2 = '../files/images/sample_1_page_changed.pdf'
        # mi = MatchImg(img1, img11)
        # mask = mi.mask()
        self.cls().compare_images(img1, img2)

    def test_compare_pdf_watermark(self):
        from doc.image.image import MatchImg
        img1 = '../files/images/sample_1_page.pdf'
        # img11 = '../files/images/000.png'
        img2 = '../files/images/sample_1_page_with_watermark.pdf'
        # mi = MatchImg(img1, img11)
        # mask = mi.mask()
        self.cls().compare_images(img1, img2)
