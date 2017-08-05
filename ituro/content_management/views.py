#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import activate, get_language, \
    LANGUAGE_SESSION_KEY
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from content_management.models import Gallery, NewsPage, CommonPage, \
    AboutPage, SponsorshipPage, CategoryPage, HomePage
from survey.models import Survey


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = "content_management/gallery_detail.html"


def HomepageRedirect(request):
    language = "/" + str(request.LANGUAGE_CODE)
    return HttpResponseRedirect(language)


def set_language(request):
    url = str(request.META.get('HTTP_REFERER'))
    unnecessary_part = str(request.scheme) + "://" + str(request.get_host())
    necessary_url = url.replace(unnecessary_part, "")
    necessary_url_args = necessary_url.split("/")
    while '' in necessary_url_args:
        necessary_url_args.remove('')
    language = str(request.POST.get('language', settings.LANGUAGE_CODE))
    activate(language)
    request.session[LANGUAGE_SESSION_KEY] = language
    if len(necessary_url_args) == 1:
        ret_obj = get_object_or_404(HomePage, language=language,
                                    sites__id__exact=settings.SITE_ID)
    else:
        category = necessary_url_args[1]
        if category == 'about' or category == 'hakkımızda':
            obj = get_object_or_404(AboutPage, url__exact=necessary_url,
                                    sites__id__exact=settings.SITE_ID)
            ret_obj = get_object_or_404(AboutPage, language=language,
                                        uid=obj.uid,
                                        sites__id__exact=settings.SITE_ID)
        elif category == 'news' or category == 'haberler':
            obj = get_object_or_404(NewsPage, url__exact=necessary_url,
                                    sites__id__exact=settings.SITE_ID)
            ret_obj = get_object_or_404(NewsPage, language=language,
                                        uid=obj.uid,
                                        sites__id__exact=settings.SITE_ID)
        elif category == 'sponsorship' or category == 'sponsorluk':
            obj = get_object_or_404(SponsorshipPage, url__exact=necessary_url,
                                    sites__id__exact=settings.SITE_ID)
            ret_obj = get_object_or_404(SponsorshipPage, language=language,
                                        uid=obj.uid,
                                        sites__id__exact=settings.SITE_ID)
        elif category == 'common' or category == 'genel':
            obj = get_object_or_404(CommonPage, url__exact=necessary_url,
                                    sites__id__exact=settings.SITE_ID)
            ret_obj = get_object_or_404(CommonPage, language=language,
                                        uid=obj.uid,
                                        sites__id__exact=settings.SITE_ID)
        elif category == 'gallery' or category == 'galeri':
            obj = get_object_or_404(Gallery, slug=necessary_url_args[2])
            ret_obj = get_object_or_404(Gallery,
                                        language=language, uid=obj.uid)
            return redirect('gallery_detail', ret_obj.slug)
        elif category == 'category':
            obj = get_object_or_404(CategoryPage, url__exact=necessary_url,
                                    sites__id__exact=settings.SITE_ID)
            ret_obj = get_object_or_404(CategoryPage, language=language,
                                        uid=obj.uid,
                                        sites__id__exact=settings.SITE_ID)
        elif category == 'survey' or category == 'anket':
            obj = get_object_or_404(Survey, slug=necessary_url_args[2],
                                    is_draft=True)
            ret_obj = get_object_or_404(Survey, language=language,
                                        uid=obj.uid)
            return redirect('survey:survey_create', ret_obj.slug)
        elif category == 'core':
            url = url.replace(necessary_url_args[0], language)
            return redirect(url)
        else:
            ret_url = url
            return redirect(ret_url)
    return redirect(ret_obj.url)
