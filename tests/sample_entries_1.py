#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# The purpose of this file is to create sample
# entries from a dictionary that contains:
# words with meanings and usage examples

from noj.data_structures import *

SAMPLE_ENTRIES_1 = list()
SAMPLE_ENTRIES_2 = list()
SAMPLE_ENTRIES_3 = list()
SAMPLE_UES_1 = list()
SAMPLE_UES_2 = list()

e = DictionaryEntry(u'\u304a\u3068\u3053\u308d', [u'\u5fa1\u6240'], u'')
m = DictionaryMeaning(u'\u3014\u76f8\u624b\u306e\u4f4f\u6240\u3092\u6307\u3057\u3066\u3015 your address.', 1)
ue = UsageExample(u'\u305d\u3053\u306b\u3042\u306a\u305f\u306e\u304a\u3068\u3053\u308d\u3068\u304a\u540d\u524d\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044.', u'Please write your name and address there.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_1.append(e)


e = DictionaryEntry(u'\u305b\u3093\u305b\u3044', [u'\u5148\u751f'], u'1')
m = DictionaryMeaning(u'\u3014\u6559\u5e2b\u3015 a teacher; a master; an instructor; \u3014\u6280\u8853\u6307\u5c0e\u8005\u3015 an instructor.', 1)
ue = UsageExample(u'\u59c9\u306f\u5c0f\u5b66\u6821\u306e\u5148\u751f\u306b\u306a\u308a\u307e\u3057\u305f.', u'My elder sister became \u2310*an elementary [\u2033a primary] school teacher.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u79c1\u306e\u30d4\u30a2\u30ce\u306f\u3061\u3083\u3093\u3068\u3057\u305f\u5148\u751f\u306b\u3064\u3044\u3066\u52c9\u5f37\u3057\u305f\u308f\u3051\u3067\u306f\u3042\u308a\u307e\u305b\u3093.', u"I didn't learn the piano with a proper teacher.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u304a\u6599\u7406\u306f\u6bcd\u3092\u5148\u751f\u306b\u3057\u3066\u7fd2\u3044\u307e\u3057\u305f.', u"I learned cooking \u2310from my mother [\u300a\u6587\u300b under my mother's tuition].", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3044\u3044\u5148\u751f\u306b\u5de1\u308a\u5408\u3048\u305f.', u'I was blessed with a good teacher. \uff5c I was lucky with \u2310my teacher [the teacher I got].', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u5f7c\u306f\u67d0\u9ad8\u6821\u306e\u5148\u751f\u3092\u3057\u3066\u3044\u308b.', u'He \u2310teaches [is a teacher] at a certain high school.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u5148\u751f, \u305d\u306e\u6b21\u306e\u884c\u306e\u610f\u5473\u304c\u308f\u304b\u308a\u307e\u305b\u3093.', u"I don't understand the next line(, teacher [Professor, \u2033Sir, \u2033Miss]). \uff5c Excuse me: I don't understand what the next line means.", 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u533b\u8005\u3015 a doctor.', 2)
ue = UsageExample(u'\u5148\u751f, \u6bcd\u306e\u5bb9\u614b\u306f\u3044\u304b\u304c\u3067\u3057\u3087\u3046.', u'How is my mother, doctor?', 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u4f5c\u5bb6, \u8b70\u54e1, \u5f01\u8b77\u58eb\u306a\u3069\u3015', 3)
ue = UsageExample(u'\u3053\u306e\u5e2d\u306b\u306f\u5f01\u8b77\u58eb\u306e\u5148\u751f\u306b\u3082\u304a\u3044\u3067\u3044\u305f\u3060\u304d\u307e\u3057\u305f.', u'\u3014\u53f8\u4f1a\u8005\u306e\u8a00\u8449\u3015 We have asked some lawyers to be present. \uff5c Our lawyers are present.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_2.append(e)



e = DictionaryEntry(u'\u3042\u3042', [u''], u'1')
m = DictionaryMeaning(u'\u3014\u554f\u3044\u306b\u7b54\u3048\u3066\u3015', 1)
ue = UsageExample(u'\u300c\u304a\u7236\u3055\u3093, \u3042\u308c\u306a\u3042\u306b\u300d\u300c\u3042\u3042, \u3042\u308c\u306f\u706f\u53f0\u3060\u3088\u300d', u'"What is that, Daddy?"\u2015"Oh, it is a lighthouse."', 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u6c17\u8efd\u306a\u80af\u5b9a\u30fb\u627f\u8afe\u3015', 2)
ue = UsageExample(u'\u300c\u3053\u308c\u501f\u308a\u3066\u3044\u3044\u3067\u3059\u304b\u300d\u300c\u3042\u3042, \u3044\u3044\u3088\u300d', u'"Can I borrow this?"\u2015"Yes, all right [\u300a\u53e3\u300b Yeah, OK]."', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u300c\u7720\u304f\u306a\u3044\u304b\u300d\u300c\u3042\u3042, \u7720\u304f\u306a\u3044\u300d', u'"Aren\'t you sleepy?"\u2015"No, I\'m not."', 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u751f\u8fd4\u4e8b\u3015', 3)
ue = UsageExample(u'\u300c\u30d1\u30d1, \u65e9\u304f\u6765\u3066\u300d\u300c\u3042\u3042, \u4eca\u884c\u304f\u3088\u300d', u'"Daddy! Come quickly!"\u2015"OK [All right], I\'m coming."', 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u8a00\u3044\u3088\u3069\u3080\u3068\u304d\u3015', 4)
ue = UsageExample(u'\u3042\u3042, \u307e\u3042, \u305d\u306e\u3053\u3068\u306a\u3089, \u307e\u3042, \u305f\u3076\u3093, \u8abf\u67fb\u3057\u3066, \u5f8c\u523b\u3054\u8fd4\u4e8b\u3092\u3055\u3057\u3042\u3052\u3089\u308c\u308b\u3068\u601d\u3044\u307e\u3059\u3088.', u'Er\u2026, well\u2026; as far as that matter is concerned\u2026perhaps\u2026er, perhaps I could look into it and let you have an answer later.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_3.append(e)

e = DictionaryEntry(u'\u3042\u3042', [u''], u'2')
m = DictionaryMeaning(u'\u3014\u611f\u52d5\u3057\u305f\u3068\u304d\u306a\u3069\u306e\u767a\u58f0\u3015 Ah!; Oh!; \u300a\u6587\u300b Alas!', 1)
ue = UsageExample(u'\u3042\u3042, \u3046\u308c\u3057\u3044.', u'Oh, I am so glad! \uff5c I am glad. \u27a1am \u306b\u5f37\u52e2\u3092\u7f6e\u304f.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u6691\u3044!', u"I am hot. \u27a1am \u306b\u5f37\u52e2\u3092\u7f6e\u304f. \uff5c Phew! Isn't it hot!", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u4eca\u65e5\u306f\u75b2\u308c\u305f.', u"Oof! It's been a hard day!", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u3069\u3046\u3057\u3088\u3046\u56f0\u3063\u305f.', u'Oh, dear! What am I to do?', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u601d\u3044\u51fa\u3057\u305f.', u'Ah! I remember (now).', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u305d\u3046\u3067\u3059\u304b.', u'Oh, really? \uff5c Really? \uff5c Oh, is that so?', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u307b\u3093\u3068\u3046\u3060. \u305d\u3063\u304f\u308a\u3060.', u"Oh! You're right. They're just alike.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u5e78\u8584\u304d\u308f\u304c\u59b9\u3088.', u'\u300a\u6587\u300b Alas [Ah, me]! My poor unfortunate sister!', 0)
m.add_usage_example(ue)
e.add_meaning(m)
m = DictionaryMeaning(u'\u3014\u547c\u3073\u304b\u3051\u3015 I say; *Say.', 2)
ue = UsageExample(u'\u3042\u3042, \u306a\u306b\u304b\u843d\u3068\u3057\u307e\u3057\u305f\u3088.', u"I say, you've dropped something!", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042, \u3082\u3057\u3082\u3057.', u'Yes, hello! \uff5c Hello, yes.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_3.append(e)

e = DictionaryEntry(u'\u3042\u3042', [u''], u'3')
m = DictionaryMeaning(u'\u3014\u3042\u306e\u3088\u3046\u306b\u3015 like that. [\u21d2<LINK>\u3042\u3042\u3044\u3046</LINK[108265:204]>]', 1)
ue = UsageExample(u'\u3042\u3042\u307e\u3067\u6709\u540d\u3068\u306f\u77e5\u3089\u306a\u304b\u3063\u305f.', u'I did not know he was \u2310so [that] famous.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042\u306f\u8a00\u3046\u3082\u306e\u306e, \u5f7c\u306f\u3084\u306f\u308a\u606f\u5b50\u304c\u304b\u308f\u3044\u3044\u306e\u3060.', u"He does love his son in spite of what he says. \uff5c That's what he says, but he loves his son \u2310all the same [in spite of that].", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042\u306a\u3063\u305f\u306e\u3082\u81ea\u696d\u81ea\u5f97\u3055.', u"He brought that on himself. \uff5c He has only himself to blame for that. \uff5c It's his own fault that it turned out that way.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042\u3057\u3066\u3053\u3046\u3057\u3066\u3068\u6bb5\u53d6\u308a\u3092\u7acb\u3066\u305f.', u'I worked out the arrangements, coming up with and rejecting one idea after another.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u5f53\u6642\u306f\u3042\u3042\u3059\u308b\u3088\u308a\u65b9\u6cd5\u304c\u306a\u304b\u3063\u305f\u306e\u3060.', u'At that time we had \u2310no alternative [no choice but to do as we did]. \uff5c At that time there was \u2310no other solution [no other way of doing it].', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u82e5\u3044\u8005\u306f\u3068\u304b\u304f\u3042\u3042\u3057\u305f\u3082\u306e\u3055.', u"That's the way young people are.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u3042\u8a00\u3048\u3070\u3053\u3046\u8a00\u3046\u4eba\u306a\u3093\u3060\u304b\u3089, \u541b\u306f.', u'You always contradict me. \uff5c You \u2310pick me up on [find fault with] everything I say. \uff5c Whatever I say, you say the opposite.', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u5f7c\u306f\u3042\u3042\u3060\u3053\u3046\u3060\u3068\u6587\u53e5\u3070\u304b\u308a\u8a00\u3063\u3066, \u5168\u7136\u624b\u4f1d\u308f\u306a\u3044.', u"He does nothing but complain about this, that and the other, and doesn't \u2310help [give us any help] at all.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u307f\u3093\u306a\u3067\u304a\u4e92\u3044\u306e\u4f5c\u54c1\u3092\u3042\u3042\u3060\u3053\u3046\u3060\u3068\u6279\u8a55\u3057\u3042\u3063\u305f.', u"We all put forward a variety of comments on each other's work.", 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u4f1a\u8b70\u306f\u3042\u3042\u3067\u3082\u306a\u3044\u3053\u3046\u3067\u3082\u306a\u3044\u3067, \u7d50\u5c40\u4f55\u3082\u6c7a\u307e\u3089\u306a\u304b\u3063\u305f.', u'One proposal after another was discussed and rejected, and the meeting \u2310ended up deciding nothing [ended up not coming to any conclusion].', 0)
m.add_usage_example(ue)
ue = UsageExample(u'\u3042\u306e\u7537\u306f\u3042\u3042\u3067\u3082\u306a\u3044\u3053\u3046\u3067\u3082\u306a\u3044\u3068\u96e3\u3057\u3044\u7537\u3060.', u'(He never seems to be satisfied.) He is a very \u2310hard [difficult] man to please.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_3.append(e)


ue = UsageExample(u'\u5f7c\u306f\u3042\u3042\u3060\u3053\u3046\u3060\u3068\u6587\u53e5\u3070\u304b\u308a\u8a00\u3063\u3066, \u5168\u7136\u624b\u4f1d\u308f\u306a\u3044.', u"He does nothing but complain about this, that and the other, and doesn't \u2310help [give us any help] at all.", 0)
SAMPLE_UES_1.append(ue)
ue = UsageExample(u'\u307f\u3093\u306a\u3067\u304a\u4e92\u3044\u306e\u4f5c\u54c1\u3092\u3042\u3042\u3060\u3053\u3046\u3060\u3068\u6279\u8a55\u3057\u3042\u3063\u305f.', u"We all put forward a variety of comments on each other's work.", 0)
SAMPLE_UES_1.append(ue)
ue = UsageExample(u'\u5f7c\u306f\u56fd\u5bb6\u3068\u76f8\u5bb9\u308c\u306a\u3044\u601d\u60f3\u306e\u6301\u3061\u4e3b\u3068\u3057\u3066\u6295\u7344\u3055\u308c\u305f.', u'He was imprisoned as someone whose ideology was incompatible with that of the state.', 0)
SAMPLE_UES_2.append(ue)

