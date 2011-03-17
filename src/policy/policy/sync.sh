#!/usr/bin/env bash
bin/i18ndude sync --pot src/policy/policy/locales/policy.pot src/policy/policy/locales/no/LC_MESSAGES/policy.po
msgfmt --no-hash -o src/policy/policy/locales/no/LC_MESSAGES/policy.mo src/policy/policy/locales/no/LC_MESSAGES/policy.po
bin/i18ndude sync --pot src/policy/policy/locales/plone.pot src/policy/policy/locales/no/LC_MESSAGES/plone.po
msgfmt --no-hash -o src/policy/policy/locales/no/LC_MESSAGES/plone.mo src/policy/policy/locales/no/LC_MESSAGES/plone.po
