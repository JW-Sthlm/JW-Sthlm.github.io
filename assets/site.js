// jw-sthlm.github.io: catalogue filters, bio language tabs, copy buttons and word counts.
(() => {
  document.querySelectorAll('[data-filter-group]').forEach((group) => {
    const list = document.getElementById(group.dataset.filterGroup);
    const count = document.getElementById(group.dataset.count);
    const noun = group.dataset.noun || 'items';
    if (!list) return;
    group.addEventListener('click', (event) => {
      const button = event.target.closest('button[data-filter]');
      if (!button) return;
      group.querySelectorAll('button[data-filter]').forEach((b) => b.setAttribute('aria-pressed', String(b === button)));
      const filter = button.dataset.filter;
      let shown = 0;
      list.querySelectorAll('[data-tags]').forEach((item) => {
        const match = filter === 'all' || item.dataset.tags.split(' ').includes(filter);
        item.hidden = !match;
        if (match) shown += 1;
      });
      list.querySelectorAll('[data-group]').forEach((section) => {
        section.hidden = !section.querySelector('[data-tags]:not([hidden])');
      });
      if (count) count.textContent = 'Showing ' + shown + ' ' + (shown === 1 ? noun.replace(/s$/, '') : noun);
    });
  });

  document.querySelectorAll('[data-words]').forEach((el) => {
    const source = document.getElementById(el.dataset.words);
    if (!source) return;
    const total = source.textContent.trim().split(/\s+/).length;
    el.textContent = total + ' ' + el.dataset.unit;
  });

  document.querySelectorAll('[data-copy]').forEach((button) => {
    button.addEventListener('click', async () => {
      const source = document.getElementById(button.dataset.copy);
      if (!source) return;
      const text = Array.from(source.querySelectorAll('p')).map((p) => p.textContent.trim()).join('\n\n');
      let copied = true;
      try { await navigator.clipboard.writeText(text); } catch (err) { copied = false; }
      if (!copied) {
        const range = document.createRange();
        range.selectNodeContents(source);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      }
      const label = button.querySelector('.label-text');
      const original = label.textContent;
      label.textContent = copied ? (button.dataset.done || 'Copied') : 'Selected, press Ctrl+C';
      button.classList.add('done');
      setTimeout(() => { label.textContent = original; button.classList.remove('done'); }, 2000);
    });
  });

  const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
  function selectTab(tab) {
    tabs.forEach((t) => {
      const selected = t === tab;
      t.setAttribute('aria-selected', String(selected));
      t.tabIndex = selected ? 0 : -1;
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !selected;
    });
  }
  tabs.forEach((tab) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', (event) => {
      if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
      const step = event.key === 'ArrowRight' ? 1 : -1;
      const next = tabs[(tabs.indexOf(tab) + step + tabs.length) % tabs.length];
      selectTab(next);
      next.focus();
    });
  });
})();
