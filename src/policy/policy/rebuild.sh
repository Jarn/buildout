#!/usr/bin/env bash
bin/i18ndude rebuild-pot --pot src/policy/policy/locales/policy.pot --create "policy" --merge src/policy/policy/locales/policy-manual.pot src/policy*
bin/i18ndude rebuild-pot --pot src/policy/policy/locales/plone.pot --create "plone" --merge src/policy/policy/locales/plone-manual.pot src/policy/policy/profiles/
