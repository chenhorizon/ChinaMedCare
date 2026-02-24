<template>
  <div class="hospital-card">
    <div class="card-image">
      <img :src="hospital.image" :alt="hospital.name" />
      <div class="card-rating">
        <svg class="star-icon" viewBox="0 0 20 20" fill="currentColor">
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
        </svg>
        <span>{{ hospital.rating }}</span>
      </div>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ hospital.name }}</h3>
      <div class="card-location">
        <svg class="location-icon" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/>
        </svg>
        {{ hospital.location }}
      </div>
      <div class="card-tags">
        <span v-for="dept in hospital.departments.slice(0, 3)" :key="dept" class="tag">
          {{ dept }}
        </span>
      </div>
      <div class="card-footer">
        <div class="card-languages">
          <svg class="globe-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6H10a3 3 0 013 3v.5a2.5 2.5 0 002.5 2.5h.5c.213 0 .417.034.61.097a6.002 6.002 0 01-8.778 6.175A4.996 4.996 0 017 15v-.5a2.5 2.5 0 00-2.5-2.5H4a.5.5 0 01-.5-.5v-.973c0-.358.072-.702.206-1.027a.5.5 0 01.626-.474z" clip-rule="evenodd"/>
          </svg>
          <span>{{ hospital.languages.join(', ') }}</span>
        </div>
        <div class="card-actions">
          <button class="btn-text">View Details</button>
          <button class="btn btn-primary btn-small">Book Now</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  hospital: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.hospital-card {
  background: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border);
  transition: all 0.2s ease;
}

.hospital-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.card-image {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.hospital-card:hover .card-image img {
  transform: scale(1.05);
}

.card-rating {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(8px);
  padding: 6px 12px;
  border-radius: 100px;
  display: flex;
  align-items: center;
  gap: 4px;
  font-weight: 700;
  color: #f59e0b;
  font-size: 14px;
  box-shadow: var(--shadow-sm);
}

.star-icon {
  width: 16px;
  height: 16px;
}

.card-content {
  padding: 24px;
}

.card-title {
  margin: 0 0 12px;
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
}

.card-location {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-secondary);
  font-size: 14px;
  margin-bottom: 16px;
}

.location-icon {
  width: 16px;
  height: 16px;
  color: var(--text-muted);
}

.card-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.tag {
  padding: 4px 10px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 500;
  border-radius: 100px;
}

.card-footer {
  border-top: 1px solid var(--border);
  padding-top: 16px;
}

.card-languages {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-secondary);
  font-size: 13px;
  margin-bottom: 16px;
}

.globe-icon {
  width: 16px;
  height: 16px;
  color: var(--text-muted);
}

.card-actions {
  display: flex;
  gap: 12px;
}

.btn-text {
  flex: 1;
  background: transparent;
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 500;
  padding: 10px 16px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border);
  transition: all 0.2s ease;
}

.btn-text:hover {
  color: var(--text-primary);
  background: var(--bg-secondary);
}

.btn-small {
  flex: 1;
  padding: 10px 16px;
  font-size: 14px;
}
</style>
